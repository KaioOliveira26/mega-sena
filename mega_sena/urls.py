from .views import GameView,ResultView, PointsView
from django.urls import path

urlpatterns = [
    path('', GameView.as_view()),
    path('result/', ResultView.as_view()),
    path('points/', PointsView.as_view()),
]
