# Shortcodes for Jekyll

This directory contains shortcodes to make common content patterns easier to use in your Jekyll blog. Shortcodes are implemented as Jekyll includes with parameters.

## Available Shortcodes

### Image Gallery

Display a responsive grid of images with optional captions.

#### Usage

```liquid
{% include shortcodes/gallery.html
  images="image1.jpg, image2.jpg, image3.jpg"
  captions="Caption 1, Caption 2, Caption 3"
  alt="Alt text 1, Alt text 2, Alt text 3"
  title="Optional gallery title"
%}
```

#### Parameters

- `images` (required): Comma-separated list of image paths (relative to /assets/ or full paths)
- `captions` (optional): Comma-separated list of captions for each image
- `alt` (optional): Comma-separated list of alt text for each image
- `title` (optional): Title for the gallery

#### Example

```liquid
{% include shortcodes/gallery.html
  images="alex_le_100k.jpg, alex_le_marathon.jpg, alex_le_with_sister_bolder_boulder.jpg"
  captions="My first 100K race, Marathon finish line, Running with my sister"
  alt="Alex at 100K race, Alex at marathon, Alex with sister at Bolder Boulder"
  title="My Running Journey"
%}
```

### Code Snippet

Display code snippets with syntax highlighting and a copy button.

#### Usage

```liquid
{% include shortcodes/code.html
  language="javascript"
  title="example.js"
  code="const hello = 'world';
  console.log(hello);"
%}
```

#### Parameters

- `code` (required): The code to display
- `language` (optional): Programming language for syntax highlighting
- `title` (optional): Title for the code snippet (e.g. filename)

#### Example

```liquid
{% include shortcodes/code.html
  language="python"
  title="hello_world.py"
  code="def say_hello():
    print('Hello, World!')
    say_hello()"
%}
```

#### Standard Markdown Code Fences

For simpler code blocks, you can also use standard markdown triple backtick syntax:

````markdown
```python
def hello():
    print('Hello, world!')

hello()
```
````

Note: This method doesn't support all features of the shortcode (like titles, copy button, or line numbers).

## Mobile-Friendly Features

These shortcodes are designed to be mobile-friendly:

1. The image gallery uses a responsive grid that adapts to screen size
2. Images use lazy loading to improve mobile performance
3. Code snippets have a copy button for easy sharing from mobile
4. All elements use appropriate font sizes for mobile readability

### Tips for Mobile Blogging with Code Snippets

When blogging from mobile devices:

1. **Use Jekyll include syntax** rather than markdown code fences for better control
2. **Format your code carefully** in the YAML parameter, keeping proper indentation
3. For complex code blocks, consider drafting in a code editor app first
4. Test how your code appears in both light and dark modes
5. You can edit your posts through GitHub's mobile interface for quick updates
