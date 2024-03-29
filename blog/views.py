from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page' , 1)
    
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)


    return render(request,
                  'blog/post/list.html',
                  {'posts' : posts}
                  )

def post_detail(request , slug, year, month, day):
    post = get_object_or_404(Post, status = Post.Status.PUBLISHED,
                             slug = slug, publish__year = year,
                             publish__month = month , publish__day = day
                             )
    # try:
    #     post = Post.published.get(id = id)
    # except Post.DoesNotExist:
    #     raise Http404('No Post Found')

    return render (request,
                   'blog/post/detail.html',
                   {'post' : post}
                   )