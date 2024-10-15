from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("add/", views.add_entry, name="add_entry"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save_edit, name="save_edit"),
    path("random/", views.random_page, name="random_page")
]
