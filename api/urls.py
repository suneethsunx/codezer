from django.urls import path
from . import views

urlpatterns = [
    path('', views.allCodes, name='all-codes'),
    path('code/<int:pk>/', views.getCode, name='get-code'),
    path('code/update/<int:pk>/', views.editCode, name='edit-code'),
    path('add-code/', views.addCode, name='add-code'),
    path('code/delete/<int:pk>/', views.deleteCode, name='delete-code'),
    
]