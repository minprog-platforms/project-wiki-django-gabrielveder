from django.shortcuts import render
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect

import random as rd
from . import util

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
    Displays requested entry page if entry exists, otherwise displays 
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

def new_page(request):
    """ 
    Displays page where users can create a new wiki entry.
    Allows for users to save the new entry on the encyclopedia.
    If user enters title which is already in use, error message is shown.
    """
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST["title"]
        body = request.POST["body"]
        # Display error if title already exists
        if util.check_title(title) == True:
            return render(request, "encyclopedia/duplicate.html")
        util.save_entry(title, body) 
        # Redirects user to created entry 
        return HttpResponseRedirect(title)

def random(request):
    """
    Redirects user to random page when clicked on the 'Random Page' button
    from anywhere on the website.
    """
    entries = util.list_entries()
    entry = rd.choice(entries)
    return HttpResponseRedirect(entry)
