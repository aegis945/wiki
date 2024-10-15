from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from random import choice

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()

    if content is None:
        return None
    else:
        return markdowner.convert(content)

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f'The requested page "{title}" was not found in encyclopedia'
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['search_query']
        html_content = convert_md_to_html(entry_search)

        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else:
            recommendations = [entry for entry in util.list_entries() if entry_search.lower() in entry.lower()]
            return render(request, "encyclopedia/search.html", {
                "recommendations": recommendations,
                "entry_search": entry_search
            })
    else:
        return redirect("encyclopedia:index")
    
def add_entry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_entry.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        already_exists = util.get_entry(title)

        if already_exists is not None:
            return render(request, "encyclopedia/error.html", {
                "message": f'The page with the title "{title}" already exists.'
            })
        else:
            util.save_entry(title, content)
            return redirect("encyclopedia:entry", title=title)
    
def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    else:
        return redirect("encyclopedia:index")
    
def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)
    else:
        return redirect("encyclopedia:index")
    
def random_page(request):
    random_entry = choice(util.list_entries())
    return redirect("encyclopedia:entry", title=random_entry)