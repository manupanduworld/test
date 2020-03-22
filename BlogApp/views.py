from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def bloghome(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request, 'bloghome.html', {'blogs': blogs})

def detail(request, BlogApp_id):
    blogs = get_object_or_404(Blog, pk=BlogApp_id)
    return render(request, 'detail.html', {'blog': blogs})