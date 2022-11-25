from django.shortcuts import render
from markdown2 import Markdown

from . import util

# views can be thought of as pages the user can see

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_title):
    content = util.get_entry(entry_title)
    if content is None:
        return render(request, "encyclopedia/error.html")
    # create Markdown object
    translate = Markdown()
    # convert markdown to html
    converted_md = translate.convert(content)
    return render(request, "encyclopedia/entry.html", {
        "entry_title": entry_title,
        "entry_body": converted_md
    })