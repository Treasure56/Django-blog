from django.shortcuts import render
# from django.http import HttpResponse
from news.models import BlogPost


def index(request):
    blogs = BlogPost.objects.order_by('-blog_date')[:5]
    popular = BlogPost.objects.filter(popular=True)[:7]
    
    context = {
        'blognews': blogs,
        'popular': popular
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

