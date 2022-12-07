from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:id>', views.Index.as_view(), name="index"),
    path('login', views.login.as_view(), name='login')
]