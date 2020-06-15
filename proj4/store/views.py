from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #, GenView
from .models import Post
import string
import random



def home(request):
    context = {
    'posts': Post.objects.filter(author=request.user),
    }
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

        return render(request, 'store/home.html', context.objects.filter(user=request.user))

class PostListView(ListView):
    model = Post
    template_name ='store/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['site', 'email', 'un', 'pw']
    success_url = '/'
    def generatePassword(num):
        password = ''
        num = 16
        for n in range(num):
    	    x = random.randint(0,94)
    	    password += string.printable[x]
        render(password)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# generate and print a 16 character random password
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['site', 'email', 'un', 'pw']
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'store/about.html', {'title' : 'About'})
