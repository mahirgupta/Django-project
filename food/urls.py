from unicodedata import name
from django.urls import path
from. import views

urlpatterns =[
    path('',views.index,name="index"),
    path('<int:item_id>',views.detail,name="detail"),
    path('create_item',views.create_item,name="create_item"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]