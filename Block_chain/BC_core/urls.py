from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     path('block_height/<int:block_id>/', views.detail_block, name='block_height'),
]