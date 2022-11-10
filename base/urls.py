from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('code/<int:pk>/',views.get_code, name='code'),
    path('get-code/<link_id>/', views.get_other_code, name='get-other-code'),
    path('search/', views.search_code, name='search'),
]
