from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id) 
    return render(request, 'detail.html', {'details' : details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() #Blog객체 생성, 생성한 객체의 이름은 blog
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()#blog작성하는 시점을 나타내는 함수
    blog.save()
    return redirect('/blog/' + str(blog.id))
