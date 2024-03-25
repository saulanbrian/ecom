from django.urls import path
from . import views

urlpatterns=[
  path('',views.orders,name='orders'),
  path('receive',views.receive_order,name='receive-order'),
  path('received',views.received_orders,name='received-orders'),
  path('cancelled',views.cancelled_orders,name='cancelled-orders'),
  path('to-receive',views.to_receive,name='to-receive'),
  path('cancel-order',views.cancel_order,name='cancel-order')
  ]