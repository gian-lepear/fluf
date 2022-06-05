from core.views import AnimalDetailView, AnimalListView
from django.urls import path

urlpatterns = [
    path("animal/", AnimalListView.as_view()),
    path("animal/<int:pk>/", AnimalDetailView.as_view()),
]
