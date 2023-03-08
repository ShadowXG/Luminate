from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Post, Like
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# index route for posts
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', { 'posts': posts })

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body']
    success_url = '/posts'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body']
    success_url = '/posts/'

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'

def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        like.delete()
    return redirect('index')

def liked_posts(request):
    liked_posts = request.user.post_likes.all()
    print(liked_posts)
    return render(request, 'likes/index.html', {'liked_posts': liked_posts})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid sign up - try again"
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)