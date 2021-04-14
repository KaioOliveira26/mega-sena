from .views import UserView, UserCreateView
from django.urls import path

urlpatterns = [
    path('', UserView.as_view()),
    path('create/', UserCreateView.as_view()),
]
