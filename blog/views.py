from django.shortcuts import render
from .models import BlogPost
from .utils import get_user_country


def post_list(request):
    client_country = get_user_country(request)
    posts = BlogPost.objects.all()
    filtered_posts=BlogPost.objects.filter(country=client_country)
    context={
        'posts':posts,
        'filtered_posts':filtered_posts,
        'country':client_country
    }
    return render(request, 'blog/post_list.html',context )

