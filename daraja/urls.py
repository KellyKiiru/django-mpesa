from django.urls import path
from . import views
from .views import TestView,index, MakePayment

urlpatterns = [
    path('', TestView.as_view(), name='testview'),
    path('index/', views.index, name='index'),
    path('api/v1/lnm_stk_push/', MakePayment.as_view(), name='makepayment'),
]
