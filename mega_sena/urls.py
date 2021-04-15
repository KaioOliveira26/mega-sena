from .views import GameView,ResultView
from django.urls import path

urlpatterns = [
    path('game/', GameView.as_view()),
    path('result/', ResultView.as_view()),
]
