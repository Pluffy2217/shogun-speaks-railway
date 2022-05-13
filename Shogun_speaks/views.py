from django.shortcuts import render, get_object_or_404
from .models import Post


def home_page(request):
    latest_posts = Post.objects.all().order_by("-date")
    featured_post = Post.objects.all().order_by("?")
    return render(request, "Shogun_speaks/index.html", {
        "posts": latest_posts,
        "featured": featured_post
    })


def Anime (request):
    all_anime_posts = Post.objects.filter(tags__caption="Anime").order_by("-date")
    return render(request, "Shogun_speaks/anime.html", {
        "all_anime_posts": all_anime_posts
    })
def anime_post_detail (request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Shogun_speaks/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })


def Manga (request):
    all_manga_posts = Post.objects.filter(tags__caption="Manga").order_by("-date")
    return render(request, "Shogun_speaks/manga.html", {
        "all_manga_posts": all_manga_posts
    })
def manga_post_detail (request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Shogun_speaks/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })


def Games (request):
    all_games_posts = Post.objects.filter(tags__caption="Games").order_by("-date")
    return render(request, "Shogun_speaks/games.html", {
        "all_games_posts": all_games_posts
    })
def games_post_detail (request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Shogun_speaks/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })


def Music (request):
    all_music_posts = Post.objects.filter(tags__caption="Music").order_by("-date")
    return render(request, "Shogun_speaks/music.html", {
        "all_music_posts": all_music_posts
    })
def music_post_detail (request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Shogun_speaks/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })


def Art (request):
    all_art_posts = Post.objects.filter(tags__caption="Art").order_by("-date")
    return render(request, "Shogun_speaks/art.html", {
        "all_art_posts": all_art_posts
    })
def art_post_detail (request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Shogun_speaks/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })


def Others (request):
    all_others_posts = Post.objects.filter(tags__caption="Others").order_by("-date")
    return render(request, "Shogun_speaks/others.html", {
        "all_others_posts": all_others_posts
    })
def others_post_detail (request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Shogun_speaks/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

def about (request):
    return render(request, "Shogun_speaks/about.html")
