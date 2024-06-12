from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from blogs import models

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"


class UserBlogsListView(LoginRequiredMixin, ListView):
    model = models.Blog
    template_name = "blogs/my_blogs.html"
    context_object_name = "user_blogs"

    def get_queryset(self):
        return models.Blog.objects.filter(author=self.request.user)
