from django.shortcuts import get_object_or_404, render
from .models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts = Post.objects.all().order_by('-published_date') # ordenar acendente
    posts = Post.objects.all().order_by('-published_date')  # ordenar decrescente
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # post = Post.objects.get(pk=chave) nao funciona porque nao sabemos se sempre sera passado um ip valido
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
