from django.shortcuts import render

def categories(request):
    cat = request.GET.get('category')
    return render(request, 'news/news.html')

def single(request, news_id):
    return render('news/single.html')
# Create your views here.
