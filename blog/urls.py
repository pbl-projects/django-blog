from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('post/<slug:slug>', views.post),
    path('category/<slug:slug>', views.category),
    path('test/bootstrap', views.test_bootstrap)
]