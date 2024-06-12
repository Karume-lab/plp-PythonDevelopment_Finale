from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog-list"),
    path("create/", views.BlogCreateView.as_view(), name="blog-create"),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="blog-detail"),
    path(
        "<slug:slug>/update/", views.BlogUpdateView.as_view(), name="blog-update"
    ),
    path(
        "<slug:slug>/delete/", views.BlogDeleteView.as_view(), name="blog-delete"
    ),
    path(
        "<slug:slug>/comment/",
        views.CommentCreateView.as_view(),
        name="comment-create",
    ),
    path('tag/<str:tag>/', views.FilteredBlogsByTagListView.as_view(), name='filtered-blogs-by-tag'),
]
