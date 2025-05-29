from django.urls import path
from .views import (ArticleListView, ArticleDetailView,
                    ArticleCreateView, ArticleUpdateView,
                    ArticleDeleteView)

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="article_edit"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
