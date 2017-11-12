from django.shortcuts import render
from .models import Articles, Classification
from django.core.paginator import Paginator

ARTICLES_NUM_PER_PAGE = 2


def get_pages_range(page, paginator):
    pages_num = paginator.num_pages
    if pages_num / page > 2:
        left = max(page - 2, 1)
        right = min(left + 4, pages_num)
    else:
        right = min(page + 2, pages_num)
        left = max(right - 4, 1)
    return paginator.page_range[left - 1: right]


def index(request, page):
    if page == '':
        page = 1
    else:
        page = int(page)
    top_articles = Articles.objects.order_by('-top')[0:3]
    paginator = Paginator(Articles.objects.order_by('-date'), ARTICLES_NUM_PER_PAGE)
    page_object = paginator.page(page)
    pages_range = get_pages_range(page, paginator)
    context = {'title': '首页', 'topArticles': top_articles, 'page_object': page_object, 'pages_range': pages_range,
               'path': '/index/'}
    return render(request, 'articles/index.html', context=context)


def share(request, tag, page):
    if page == '':
        page = 1
    else:
        page = int(page)

    tag = int(tag)
    if tag == 1:
        paginator = Paginator(Articles.objects.filter(classification__parent__name='share').order_by('-date'),
                              ARTICLES_NUM_PER_PAGE)
    else:
        paginator = Paginator(Articles.objects.filter(classification=tag), ARTICLES_NUM_PER_PAGE)
    page_object = paginator.page(page)
    pages_range = get_pages_range(page, paginator)
    tags = Classification.objects.get(pk=1).classification_set.values_list('id', 'name')
    context = {'title': '分享', 'tags': tags, 'page_object': page_object, 'pages_range': pages_range,
               'path': '/articles/share/' + str(tag) + '/'}
    return render(request, 'articles/share.html', context=context)


def note(request, page):
    if page == '':
        page = 1
    else:
        page = int(page)
    paginator = Paginator(Articles.objects.filter(classification__name='note').order_by('-date'), ARTICLES_NUM_PER_PAGE)
    page_object = paginator.page(page)
    pages_range = get_pages_range(page, paginator)
    context = {'title': '笔记', 'page_object': page_object, 'pages_range': pages_range, 'path': '/articles/note/'}
    return render(request, 'base_timeline.html', context=context)


def life(request, page):
    if page == '':
        page = 1
    else:
        page = int(page)
    paginator = Paginator(Articles.objects.filter(classification__name='life').order_by('-date'), ARTICLES_NUM_PER_PAGE)
    page_object = paginator.page(page)
    pages_range = get_pages_range(page, paginator)
    context = {'title': '生活', 'page_object': page_object, 'pages_range': pages_range, 'path': '/articles/life/'}
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
