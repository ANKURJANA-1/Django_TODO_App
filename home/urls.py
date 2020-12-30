
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('submit',views.submit,name="submit"),
    path('seen',views.seen,name="seen"),
]
