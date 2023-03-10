from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Like, Reply, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse
import uuid # pthon pakage for creating unique identifiers
import boto3 # what we'll use to connect to s3
from django.conf import settings

AWS_ACCESS_KEY = settings.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
S3_BUCKET = settings.S3_BUCKET
S3_BASE_URL = settings.S3_BASE_URL

# Create your views here.
def home(request):
    return render(request, 'home.html')

# index route for posts
def posts_index(request):
    posts = Post.objects.prefetch_related('replies').all
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
        return redirect('liked_posts')
    return redirect('index')

def liked_posts(request):
    liked_posts = request.user.post_likes.all()
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

def add_reply(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        reply = Reply(content=content, user=request.user, post=post )
        reply.save()
        return redirect('index')

class ReplyUpdate(UpdateView):
    model = Reply
    fields = ['content']
    template_name_suffix = '_form'
    success_url = '/posts/'

    # def get_success_url(self):
    #     return reverse('index', args=[self.object.post.id])

class ReplyDelete(DeleteView):
    model = Reply
    success_url = '/posts/'

def add_photo(request, post_id):
    # photo-file will be the name attribute of our form input
    photo_file = request.FILES.get('photo-file', None)
    # use conditional logic to make sure a file is present
    if photo_file:
        # S3_BASE_URL
        # if present, we'll use this to create a reference to the boto3 client
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        # create a uniqu key for our photos
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            # if success
            s3.upload_fileobj(photo_file, S3_BUCKET, key)
            # build the full url string to upload the s3
            url = f"{S3_BASE_URL}{S3_BUCKET}/{key}"
            # if our upload was successful
            # we want to ust that photo location to creat a Photo model
            photo = Photo(url=url, post_id=post_id)
            # save the photo to the db
            photo.save()
        except Exception as error:
            # print an error message
            print('Error uploading photo', error)
            return redirect('index')
        
    return redirect('index')