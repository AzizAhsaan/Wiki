from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entrymethod, name="entrymethod"),
    path("search/", views.searchbar, name="searchbar"),
    path("newpage/",views.newpage, name="newpage"),
    path("editpage/", views.editpage ,name="editpage"),
    path("thenewedit/",views.thenewedit ,name="thenewedit"),
    path("randompage/",views.randompage, name="randompage")
]
