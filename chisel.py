import sys, re, time, os, getopt, datetime, glob, itertools, BaseHTTPServer
import jinja2, markdown
from SimpleHTTPServer import SimpleHTTPRequestHandler

# Settings
SOURCE = "./posts/"
DESTINATION = "./blog/"
HOME_SHOW = 12
TEMPLATE_PATH = "./templates/"
TEMPLATE_OPTIONS = {}
TEMPLATES = {
   'home': "home.html",
   'post': "post.html",
   'archive': "archive.html",
   'about': "about.html",
   'photos': "photos.html",
   'rss': "rss.html",
   'sitemap': "sitemap.html",
   'htaccess': "htaccess.txt",
}
TIME_FORMAT = "%b %d, %Y"
ENTRY_TIME_FORMAT = "%m-%d-%Y"
RSS_TIME_FORMAT = "%a, %d %b %Y 00:00:00 MST"
STEPS = []

# FORMAT should be a callable that takes in text and returns formatted text
FORMAT = lambda text: markdown.markdown(text, ['footnotes',])

# Template Blog Info
class TemplateBlogInfo:
    def __init__( self, css_raw ):
        self.css_raw = css_raw
    cp_year = datetime.datetime.now().year
    incl_prism = True

def CreateCSSRaw( ):
    css_raw = []
    files = glob.glob('./css/*.css')
    for file in files:
        f = open(file, 'r')
        css_raw.append( f.read().split('\n') )
        f.close()
    css_raw_flat = list(itertools.chain.from_iterable(css_raw))
    return ''.join(css_raw_flat)

# Post Header Info
class PostHeaderInfo:
    title = ''
    raw_date = ''
    image = ''
    meta = ''

def ParsePostHeader( f ):
    # Read off first '---' tag.
    f.readline().rstrip()
    H = PostHeaderInfo()
    line = ''
    while '---' not in line:
        line = f.readline().rstrip()
        if line.startswith('title'):
            H.title = line.replace('title:', '').lstrip()
        if line.startswith('date'):
            H.raw_date = line.replace('date:', '').lstrip()
        if line.startswith('image'):
            H.image = line.replace('image:', '').lstrip()
        if line.startswith('meta'):
            H.meta = line.replace('meta:', '').lstrip()
    return H

def step(func):
   def wrapper(*args, **kwargs):
      print "\tStarting " + func.__name__ + "..."
      func(*args, **kwargs)
   STEPS.append(wrapper)
   return wrapper

def get_tree(source):
   files = []
   for root, ds, fs in os.walk(source):
      for name in fs:
         if name[0] == ".": continue
         path = os.path.join(root, name)
         f = open(path, "rU")

         Header = ParsePostHeader( f )
         date = time.strptime(Header.raw_date, ENTRY_TIME_FORMAT)
         year, month, day = date[:3]
         epoch = time.mktime(date)

         # If post is newer than 10-01-2013, use new URL format
         if epoch > 1380607200.0:
            url = '/'.join([os.path.splitext(name)[0] + ".html"])
         else:
            url = '/'.join([str(year), os.path.splitext(name)[0] + ".html"])

         files.append({
            'title': Header.title,
            'epoch': epoch,
            'content': FORMAT(''.join(f.readlines()[1:]).decode('UTF-8')),
            'url': url,
            'pretty_date': time.strftime(TIME_FORMAT, date),
            'year': year,
            'month': month,
            'day': day,
            'filename': name,
            'rss_date': time.strftime(RSS_TIME_FORMAT, date),
            'img': Header.image,
            'meta': Header.meta
         })
         f.close()
   return files

def compare_entries(x, y):
   result = cmp(-x['epoch'], -y['epoch'])
   if result == 0:
      return -cmp(x['filename'], y['filename'])
   return result

def write_file(url, data):
   path = DESTINATION + url
   dirs = os.path.dirname(path)
   if not os.path.isdir(dirs):
      os.makedirs(dirs)
   file = open(path, "w")
   file.write(data.encode('UTF-8'))
   file.close()

@step
def generate_homepage(f, e, b):
   b.incl_prism = False
   """Generate homepage"""
   template = e.get_template(TEMPLATES['home'])
   write_file("../index.html", template.render(entries=f[:HOME_SHOW], blog_info=b))

@step
def master_archive(f, e, b):
   b.incl_prism = False
   """Generate master archive list of all entries"""
   template = e.get_template(TEMPLATES['archive'])
   write_file("archives.html", template.render(entries=f, blog_info=b))

@step
def detail_pages(f, e, b):
   """Generate detail pages of individual posts"""
   template = e.get_template(TEMPLATES['post'])
   for file in f:
      write_file(file['url'], template.render(entry=file, blog_info=b))

@step
def generate_about(f, e, b):
   b.incl_prism = False
   """Generate about page"""
   template = e.get_template(TEMPLATES['about'])
   write_file("../about.html", template.render(entries=f, blog_info=b))

@step
def generate_photos(f, e, b):
   b.incl_prism = False
   """Generate photos page"""
   template = e.get_template(TEMPLATES['photos'])
   write_file("../photos.html", template.render(entries=f, blog_info=b))

@step
def generate_rss(f, e, b):
   """Generate rss feed"""
   template = e.get_template(TEMPLATES['rss'])
   write_file("../rss.xml", template.render(entries=f))

@step
def generate_sitemap(f, e, b):
   """Generate sitemap"""
   template = e.get_template(TEMPLATES['sitemap'])
   write_file("../sitemap.xml", template.render(entries=f))

@step
def generate_htaccess(f, e, b):
   """Generate htaccess"""
   template = e.get_template(TEMPLATES['htaccess'])
   write_file("../.htaccess", template.render(entries=f))

def chisel():
   print "Reading files..."
   files = sorted(get_tree(SOURCE), cmp=compare_entries)
   env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)
   blog_info = TemplateBlogInfo( CreateCSSRaw() )
   print "Running steps..."
   for step in STEPS:
      step(files, env, blog_info)
   print "\tDone."

def main():
   opts, args = getopt.getopt(sys.argv[1:], "s", ["server"])

   for opt, arg in opts:
      if opt in ("-s", "--server"):
         SimpleHTTPRequestHandler.protocol_version = "HTTP/1.0"
         httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)

         sa = httpd.socket.getsockname()
         print "Serving HTTP on", sa[0], sa[1], "..."
         httpd.serve_forever()

   chisel()

if __name__ == "__main__":
   sys.exit(main())
