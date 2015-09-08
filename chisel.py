#!/usr/bin/python

import sys, re, time, os, getopt, BaseHTTPServer
import jinja2, markdown
from SimpleHTTPServer import SimpleHTTPRequestHandler

# Settings
SOURCE = "./posts/"
DESTINATION = "./blog/"
HOME_SHOW = 15
TEMPLATE_PATH = "./templates/"
TEMPLATE_OPTIONS = {}
TEMPLATES = {
   'home': "home.html",
   'post': "post.html",
   'archive': "archive.html",
   'rss': "rss.html",
}
TIME_FORMAT = "%b %d, %Y"
ENTRY_TIME_FORMAT = "%m-%d-%Y"
RSS_TIME_FORMAT = "%a, %d %b %Y 00:00:00 MST"

# FORMAT should be a callable that takes in text and returns formatted text
FORMAT = lambda text: markdown.markdown(text, ['footnotes',]) 

STEPS = []

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
         title = f.readline().rstrip()
         date = time.strptime(f.readline().strip(), ENTRY_TIME_FORMAT)
         year, month, day = date[:3]
         epoch = time.mktime(date)

         # If post is newer than 10-01-2013, use new URL format
         if epoch > 1380607200.0:
            url = '/'.join([os.path.splitext(name)[0] + ".html"]) 
         else:
            url = '/'.join([str(year), os.path.splitext(name)[0] + ".html"])

         files.append({
            'title': title,
            'epoch': epoch,
            'content': FORMAT(''.join(f.readlines()[1:]).decode('UTF-8')),
            'url': url,
            'pretty_date': time.strftime(TIME_FORMAT, date),
            'year': year,
            'month': month,
            'day': day,
            'filename': name,
            'rss_date': time.strftime(RSS_TIME_FORMAT, date),
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
def generate_homepage(f, e):
   """Generate homepage"""
   template = e.get_template(TEMPLATES['home'])
   write_file("../index.html", template.render(entries=f[:HOME_SHOW]))

@step
def master_archive(f, e):
   """Generate master archive list of all entries"""
   template = e.get_template(TEMPLATES['archive'])
   write_file("archives.html", template.render(entries=f))

@step
def detail_pages(f, e):
   """Generate detail pages of individual posts"""
   template = e.get_template(TEMPLATES['post'])
   for file in f:
      write_file(file['url'], template.render(entry=file))

@step
def generate_rss(f, e):
   """Generate rss feed"""
   template = e.get_template(TEMPLATES['rss'])
   write_file("../feed.xml", template.render(entries=f))

def chisel():
   print "Reading files..."
   files = sorted(get_tree(SOURCE), cmp=compare_entries)
   env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)
   print "Running steps..."
   for step in STEPS:
      step(files, env)
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
