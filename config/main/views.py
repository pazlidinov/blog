from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Article, Tag, Category

# Create your views here.


def home_page(request):
    return render(request, 'index.html')


class List_articles(ListView):
    model = Article
    template_name = 'list_articles.html'


class Detail_Article(DetailView):
    model = Article
    template_name = 'detail_article.html'


def sort_by_teg(request, slug):
    tag=Tag.objects.get(slug=slug)
    art=Article.objects.filter(tag=tag)
    data={
        'object_list':art,
    }
    return render(request, 'list_articles.html', context=data)

def sort_by_category(request, slug):
    cat=Category.objects.get(slug=slug)
    art=Article.objects.filter(category=cat)
    data={
        'object_list':art,
    }
    return render(request, 'list_articles.html', context=data)
 
