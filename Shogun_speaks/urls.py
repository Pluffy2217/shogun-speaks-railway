from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),

    path("Anime", views.Anime, name="anime-posts"),
    path("Anime/<slug:slug>", views.anime_post_detail, name="anime-post-detail"),

    path("Manga", views.Manga, name="manga-posts"),
    path("Manga/<slug:slug>", views.manga_post_detail, name="manga-post-detail"),

    path("Games", views.Games, name="games-posts"),
    path("Games/<slug:slug>", views.games_post_detail, name="games-post-detail"),

    path("Music", views.Music, name="music-posts"),
    path("Music/<slug:slug>", views.music_post_detail, name="music-post-detail"),

    path("Art", views.Art, name="art-posts"),
    path("Art/<slug:slug>", views.art_post_detail, name="art-post-detail"),

    path("Others", views.Others, name="others-posts"),
    path("Others/<slug:slug>", views.others_post_detail, name="others-post-detail"),

    path("about", views.about, name="about")
]
    