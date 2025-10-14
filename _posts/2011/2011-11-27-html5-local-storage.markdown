---
layout: post
title: "Store your data with HTML5 local storage"
date: 2011-11-27
tags: programming
---

[Local storage][3] is a pretty cool feature included in HTML5.

It allows data to be stored on the client-side via a simple key/value database. Data saved by a page, up to 5MB, resides in the user's browser and is accessible only by pages from the same domain. In other words, local storage data saved by apple.com cannot be accessed by orange.com.

Keys can be initialized with the API, square bracket, or dot notation:

``` html
$ localStorage.setItem('name', 'Alex')

$ localStorage['name'] = 'Alex'

$ localStorage.name = 'Alex'
```

Keys can be read by the same methods. To retrieve the 'name' key's value:

``` html
$ localStorage.getItem('name')
Alex

$ localStorage['name']
Alex

$ localStorage.name
Alex
```

.clear() removes all keys and values in the domain's local storage:

``` html
$ localStorage.clear()

$ localStorage.getItem('name'))
undefined
```

Other API functions include:

* .removeItem(key)
* .key(index)
* .length

Here's a simple [demo][1] I threw together. The code is available at [github][2]. It's an editable list whose values can be saved to local storage. If applicable, the list is populated with these values every time the page is reloaded or re-opened!

There are plenty of reasons to use web storage. The state of an application can be saved, data can be cached to improve performance, user preferences can be stored, page counts can be tracked. The use-cases are endless.

What about cookies, don't they achieve the same result? Yes. But cookies have their limitations, such as being restricted to 4KB and having overhead from every server request.

Local storage is an up-and-coming technology that's powerful and easy to use. Play around with it, you might be surprised what you can do with it.

[1]: /localstorage_demo/
[2]: https://github.com/alexle/localstorage_demo
[3]: http://diveintohtml5.info/storage.html
