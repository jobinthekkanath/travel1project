from django.urls import path
from . import views
urlpatterns=[
    path('',views.fun,name='fun'),
    path('',views.fun,name='fun1'),
    path('add',views.addition,name='add')
]