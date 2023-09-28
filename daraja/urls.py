from django.urls import path
from . import views
from .views import TestView,index

urlpatterns = [
    path('', TestView.as_view(), name='testview'),
    path('index/', views.index, name='index'),
]
