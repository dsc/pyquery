# PyQuery: a jQuery-like library for Python

PyQuery allows you to make [jQuery](http://jquery.com)-style CSS-selector queries on XML/HTML
documents. The API is intended to match [jQuery's API](http://api.jquery.com) whenever possible,
though it has been made more Pythonic where appropriate.

This [project](https://github.com/dsc/pyquery) is a fork of the [original](http://www.bitbucket.org/olauzanne/pyquery) 
PyQuery developed by Olivier Lauzanne in 2008; it is maintained by [David Schoonover](mailto:dsc@less.ly). Feedback and bug
reports are both very welcome over on [github](https://github.com/dsc/pyquery/issues).


## Quickstart

You can use the PyQuery class to load an xml document from a string, a lxml
document, from a file or from an url:

    >>> from pyquery import PyQuery as pq
    >>> from lxml import etree
    >>> import urllib
    >>> d = pq("<html></html>")
    >>> d = pq(etree.fromstring("<html></html>"))
    >>> d = pq(url='http://google.com/')
    >>> # d = pq(url='http://google.com/', opener=lambda url: urllib.urlopen(url).read())
    >>> d = pq(filename=path_to_html_file)

Now `d` is like the `$` object in jQuery:

    >>> d("#hello")
    [<p#hello.hello>]
    >>> p = d("#hello")
    >>> print(p.html())
    Hello world !
    >>> p.html("you know <a href='http://python.org/'>Python</a> rocks")
    [<p#hello.hello>]
    >>> print(p.html())
    you know <a href="http://python.org/">Python</a> rocks
    >>> print(p.text())
    you know Python rocks

You can use some of the pseudo classes that are available in jQuery but that
are not standard in css such as `:first`, `:last`, `:even`, `:odd`, `:eq`, 
`:lt`, `:gt`, `:checked`, `:selected`, and `:file`.

    >>> d('p:first')
    [<p#hello.hello>]


##  Notes

 * PyQuery uses lxml for fast XML and HTML manipulation.
 * This is not a library to produce or interact with JavaScript code. If
that's what you need, check out
