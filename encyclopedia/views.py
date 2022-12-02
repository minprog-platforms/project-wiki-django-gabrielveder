from django.shortcuts import render
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

# views can be thought of as pages the user can see

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_title):
    """ 
    Displays entry page if entry exists, 404 error otherwise. 
    """

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

def search(request):
    """ 
    Displays requested entry if entry exists, otherwise displays 
    substring results.
    """
    entries = util.list_entries()
    query = request.POST["q"]
    if query in entries:
        return HttpResponseRedirect(query)
    else:
        return render(request, "encyclopedia/search_results.html", {
        "results": util.substring(query)
    })

# def new_page(request):

