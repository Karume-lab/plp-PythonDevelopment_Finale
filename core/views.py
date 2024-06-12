from django.shortcuts import render
from django.shortcuts import render
from blogs import models


def landing(request):
    return render(request, "landing/index.html")


def home(request):
    blogs = models.Blog.objects.all()
    return render(request, "core/index.html", {"blogs": blogs})
