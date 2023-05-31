from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView
from .models import Article, Tag, Category, Comment, Reply_Comment

# Create your views here.

# Artcile


def home_page(request):
    return render(request, 'index.html')


class List_articles(ListView):
    model = Article
    template_name = 'list_articles.html'


class Detail_Article(DetailView):
    model = Article
    template_name = 'detail_article.html'

# sort


def sort_by_teg(request, slug):
    tag = Tag.objects.get(slug=slug)
    art = Article.objects.filter(tag=tag)
    data = {
        'object_list': art,
    }
    return render(request, 'list_articles.html', context=data)


def sort_by_category(request, slug):
    cat = Category.objects.get(slug=slug)
    art = Article.objects.filter(category=cat)
    data = {
        'object_list': art,
    }
    return render(request, 'list_articles.html', context=data)


def sort_by_title(request):
    art = Article.objects.filter(title__icontains=request.GET.get('title'))
    data = {
        'object_list': art,
    }
    return render(request, 'list_articles.html', context=data)


def sort_by_author(request, id):
    author = User.objects.get(id=id)
    art = Article.objects.filter(author=author)
    data = {
        'object_list': art,
    }
    return render(request, 'list_articles.html', context=data)


def sort_by_published(request, published):
    art = Article.objects.filter(published=published)
    data = {
        'object_list': art,
    }
    return render(request, 'list_articles.html', context=data)


# Comment


def create_comment(request, id):
    art = Article.objects.get(id=id)
    # print(dir(request.POST.get("comment")))
    print(request.POST.dict)
    if request.method == "POST":
        comment = request.POST.get("comment")
        u = None
        if request.user.is_authenticated:
            u = request.user
        else:
            u = None

        if len(comment) > 3:
            Comment.objects.create(article=art, user=u, comment=comment)

    return redirect("home:detail", id)


def delete_comment(request, id):
    com = Comment.objects.get(id=id)
    com.delete()
    return redirect("home:detail", com.article.id)


def replay_comment(request, id):
    com = Comment.objects.get(id=id)
    if request.method == "POST":
        comment = request.POST.get("reply_comment")
        u = None
        if request.user.is_authenticated:
            u = request.user
        else:
            u = None

        if len(comment) > 3:
            Reply_Comment.objects.create(
                for_comment=com, user=u, replay_comment=comment)

    return redirect("home:detail", com.article.id)


def delete_replay_comment(request, id):
    com = Reply_Comment.objects.get(id=id)
    com.delete()
    return redirect("home:detail", com.for_comment.article.id)
