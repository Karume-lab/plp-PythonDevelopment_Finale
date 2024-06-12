from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models


class BlogListView(ListView):
    model = models.Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related("comment_set")
        for blog in queryset:
            blog.first_three_comments = blog.comment_set.all()[:3]
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = models.Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = models.Blog
    template_name = "blogs/blog_form.html"
    fields = ["title", "content", "image", "tags"]
    success_url = reverse_lazy("blogs:blog-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Blog
    template_name = "blogs/blog_form.html"
    fields = ["title", "content", "image"]
    success_url = reverse_lazy("blogs:blog-list")


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blogs:blog-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = "blogs/comment_form.html"
    fields = ["content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = models.Blog.objects.get(slug=self.kwargs["slug"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blogs:blog-detail", kwargs={"slug": self.kwargs["slug"]})


class FilteredBlogsByTagListView(ListView):
    model = models.Blog
    template_name = "filtered_blogs.html"
    context_object_name = "blogs"

    def get_queryset(self):
        tag = self.kwargs["tag"]
        return models.Blog.objects.filter(tags__name=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context
