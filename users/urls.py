from django.urls import path
from .views import RegisterView, LoginView, TestprotectedView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('test/', TestprotectedView.as_view()),
]