from django.shortcuts import render
from .models import Articles


def index(request):
    topArticles = Articles.objects.order_by('-top')[0:3]
    articles = Articles.objects.order_by('-date')
    context = {'title': '首页', 'topArticles': topArticles, 'articles': articles}
    return render(request, 'articles/index.html', context=context)


def share(request):
    articles = Articles.objects.filter(classification__parent__name='share').order_by('-date')
    context = {'title': '分享', 'articles': articles}
    return render(request, 'articles/share.html', context=context)


def note(request):
    articles = Articles.objects.filter(classification__name='note').order_by('-date')
    context = {'title': '笔记', 'articles': articles}
    return render(request, 'base_timeline.html', context=context)


def life(request):
    articles = Articles.objects.filter(classification__name='life').order_by('-date')
    context = {'title': '生活', 'articles': articles}
    return render(request, 'articles/life.html', context=context)


def about(request):
    return render(request, 'articles/about.html')


def detail(request, article_id):
    article = Articles.objects.get(id=article_id)
    if article.classification.parent is not None:
        articles = Articles.objects.filter(classification__parent=1)
    else:
        articles = Articles.objects.filter(classification=article.classification)
        # main_classification = article.classification

    title = article.title + '-丁先杰的个人博客'
    context = {'title': title, 'article': article}
    return render(request, 'articles/detail.html', context)
