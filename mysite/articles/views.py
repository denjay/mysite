from django.shortcuts import render
from .models import Articles, Classification


def index(request):
    top_articles = Articles.objects.order_by('-top')[0:3]
    articles = Articles.objects.order_by('-date')
    context = {'title': '首页', 'topArticles': top_articles, 'articles': articles}
    return render(request, 'articles/index.html', context=context)


def share(request, tag):
    tag = int(tag)
    if tag == 1:
        articles = Articles.objects.filter(classification__parent__name='share').order_by('-date')
    elif tag >= 4:
        articles = Articles.objects.filter(classification=tag)
    tags = Classification.objects.get(pk=1).classification_set.values_list('id', 'name')
    context = {'title': '分享', 'articles': articles, 'tags': tags}
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
    return render(request, 'articles/about.html', context={'title': '关于我'})


def detail(request, article_id):
    article_id = int(article_id)
    article = Articles.objects.get(id=article_id)
    article.click += 1
    article.save()

    if article.classification.parent is not None:
        articles = Articles.objects.filter(classification__parent=1)
    else:
        articles = Articles.objects.filter(classification=article.classification)

    id_list = articles.order_by('id').values_list('id', flat=True)
    previous_list = list(filter(lambda x: x < 0, map(lambda x: x - article_id, id_list)))
    previous_article = next_article = None
    if previous_list:
        previous_id = previous_list[-1] + article_id
        previous_article = Articles.objects.get(id=previous_id)
    next_list = list(filter(lambda x: x > 0, map(lambda x: x - article_id, id_list)))
    if next_list:
        next_id = next_list[0] + article_id
        next_article = Articles.objects.get(id=next_id)

    title = article.title + '-丁先杰的个人博客'
    context = {'title': title, 'article': article, 'previous_article': previous_article, 'next_article': next_article}
    return render(request, 'articles/detail.html', context)
