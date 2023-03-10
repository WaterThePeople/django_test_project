from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from .forms import CommentForm




from django.template import RequestContext
from django.shortcuts import render

def handler404(request):
    response = render('404.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'home_page/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'home_page/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AddCommentView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'home_page/add_comment.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = '/'


def welcome(request):
    return render(request,'home_page/welcome.html',{'title':'Welcome'})