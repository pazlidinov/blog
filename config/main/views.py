from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from .models import Article, Tag, Category, Comment

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


# Comment


def create_comment(request, id):
    art = Article.objects.get(id=id)

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


def delete_comment(request, comment_id):
    com = Comment.objects.get(pk=comment_id)
    com.delete()
    return redirect("home:detail", com.product.id)
