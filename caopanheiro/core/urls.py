from core.views import (
    AnimalDetailView,
    AnimalListView,
    PostDetailView,
    PostListView,
)
from django.urls import path

urlpatterns = [
    path("animal/", AnimalListView.as_view()),
    path("animal/<int:pk>/", AnimalDetailView.as_view()),
    path("post/", PostListView.as_view()),
    path("post/<int:pk>/", PostDetailView.as_view()),
]
