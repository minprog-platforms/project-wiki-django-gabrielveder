from django.shortcuts import render

from . import util

# views can be thought of as pages the user can see

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

