from django.shortcuts import render, get_list_or_404
from . models import BlogPost

def categories(request):
    cat = request.GET.get('category')
    if cat:
        blogs = BlogPost.objects.filter(category=cat)
    else:
     Blogs = BlogPost.objects.all()
    
    context = {
        'blognews': blogs,
        'category': cat
    }
    
    
    return render(request, 'news/news.html')


def single(request, news_id):
    
    blog = get_list_or_404(BlogPost, pk=news_id)
    
    context = {
        'blog': blog
    }
    
    return render(request, 'news/single.html', context)



