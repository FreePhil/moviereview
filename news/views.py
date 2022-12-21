from django.shortcuts import render

from news.models import News


def news(request):
    newses = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newses': newses})
