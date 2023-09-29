from django.urls import path
from . import views
from .views import TestView,index, MakePayment

urlpatterns = [
    path('test', TestView.as_view(), name='testview'),
    path('', views.index, name='index'),
    path('api/v1/lnm_stk_push/', MakePayment.as_view(), name='makepayment'),
]
