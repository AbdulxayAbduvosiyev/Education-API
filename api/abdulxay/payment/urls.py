from django.urls import path
from .views import PaymentListView

urlpatterns = [
    path('payment_list/', PaymentListView.as_view(), name='payment_list')
]
