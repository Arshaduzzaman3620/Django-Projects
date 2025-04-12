from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home_view,name='home'), #Home View
    path('create/',views.product_create_view,name='product_create'), #Create Product View
    path('list/',views.product_list_view,name='product_list'), #Read Product View
    path('update/<int:product_id>/',views.product_update_view,name='product_update'), #Update Product View
    path('delete/<int:product_id>/',views.product_delete_view,name='product_delete'),
    
]