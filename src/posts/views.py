from django.shortcuts import render , get_object_or_404 , redirect #importar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment, User_model 
from .forms import PostForm, CommentForm, LogInForm, SignUpForm, SignUp_Form #importar
from django.contrib.auth import authenticate, login, logout #importar
from django.contrib.auth.decorators import login_required #importar
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin #importar


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials',
                'form' : LogInForm,
            })

    return render(request, 'login.html', {'form' : LogInForm})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    
    if request.method == "POST":
        form = SignUp_Form(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('login')        
    else:
        form = SignUp_Form()

    return render(
        request,
        "signup.html",{
            'form': SignUp_Form,
            'message' : 'error'})

class PostListView(LoginRequiredMixin,ListView):
    model = Post

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail' , slug = post.slug )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form' : CommentForm()
        })
        return context

    def get_object(self, **kwargs):  
        object = super().get_object(**kwargs)
        #if self.request.user.is_authenticated: # validacion de usuario creado
        PostView.objects.get_or_create(user=self.request.user , post=object)
        return object


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'create'
        })    
        
        return context 
     

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'update'
        })
        
        return context 
    
class PostDeleteView (LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'

def like(request , slug):
    post = get_object_or_404(Post , slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail' , slug = slug )
    Like.objects.create(user=request.user, post=post)
    return redirect('detail' , slug = slug )

def error_404(request, exception):
    return render(request, '404.html')