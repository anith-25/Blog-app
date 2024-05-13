from django.shortcuts import render
from django.views.generic import ListView, DetailView,DeleteView
from django.views import View
from .models import Blog
from django.contrib.auth import get_user_model
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q

User = get_user_model()

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/blog-list.html"
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get("search")
        blogs = Blog.objects.all().order_by("-publication_date")
        if search:
            blogs = blogs.filter(Q(title__icontains=search)|Q(content__icontains=search)).order_by("-publication_date")
        return blogs

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog/blog-detail.html"


class BlogCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = BlogForm()
        return render(request, "blog/blog-edit.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST)
        if form.is_valid():
            Blog.objects.create(title=form.cleaned_data["title"], content=form.cleaned_data["content"], author=request.user)
            return redirect("blog_list")
        return render(request, "blog/blog-edit.html", {"form": form})


class BlogUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(author=request.user), pk=pk)
        form = BlogForm(instance=blog)
        return render(request, "blog/blog-edit.html", {"form": form})
    
    def post(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(author=request.user), pk=pk)
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
        return render(request, "blog/blog-edit.html", {"form": form})
    

class BlogDeleteView(LoginRequiredMixin, View):   
    def post(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(author=request.user), pk=pk)
        blog.delete()
        return redirect("blog_list")

