from django.urls import path

from . import views

urlpatterns = [
    path("elements/", views.elements, name="elements"),
    path("generic/", views.generic, name="generic"),
    path("shannon-fano/", views.shannon_fano_view, name="shannon_fano_view"),
    path("huffman/", views.huffman_view, name="huffman_view"),
    path(
        "meme-generator/",
        views.meme_generator_view,
        name="meme_generator_view",
    ),
    path("", views.home, name="home"),
]
