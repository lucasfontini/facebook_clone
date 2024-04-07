from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Post , Like 

# Create your views here.



@login_required(login_url="/login")
def home(request):
    user_profile = request.user.userprofile
    name = request.user
    username = name.username
    posts = Post.objects.all()
    id = name.id    
    context = {'user': username, 'id':id, 'posts':posts, 'user_profile':user_profile}
    return render(request, 'home.html', context)

class LoginView(TemplateView):
    template_name = "login.html"

def LoginSubmit(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Ação realizada com sucesso!')
            return redirect('home')
    messages.MessageFailure(request, 'error!')
    return redirect('login')  # Redirects back to login page if login fails

def Logout(request, id):
    if id: 
        logout(request)
        messages.success(request, 'Ação realizada com sucesso!')
        return redirect('login')
    
def MyProfile(request, id):
    user_profile = request.user.userprofile
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author=user)
    return render(request, "my_profile.html", {'posts': posts, 'user_profile':user_profile})


def Create_post(request):
    if request.method == 'POST':
        post_content = request.POST.get('post_content', '') 
        author = request.user
        post = Post.objects.create(content=post_content, author=author)
        posts = Post.objects.filter(author=author)
        user_profile = request.user.userprofile
        messages.success(request, 'Ação realizada com sucesso!')
        return render(request , "my_profile.html" , {'posts': posts, 'user_profile':user_profile})
    else:
        render(request , "my_profile.html")



def LikePost(request, id ):
    post = get_object_or_404(Post, id=id)
    user = request.user
    Like.objects.create(post=post, user=user)  # Assuming you have a ForeignKey from Like to Post
    return redirect('home')


def DeletePost(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')  # Redirecting to home after deleting the post


def Chat(request):
    return render(request, "chat.html") 