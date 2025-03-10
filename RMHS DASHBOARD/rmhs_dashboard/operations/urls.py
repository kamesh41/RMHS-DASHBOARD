from django.urls import path
from . import views

app_name = 'operations'

urlpatterns = [
    # Area-1 Operations
    path('area1/', views.area1_list, name='area1_list'),
    path('area1/create/', views.area1_create, name='area1_create'),
    path('area1/<int:pk>/', views.area1_detail, name='area1_detail'),
    path('area1/<int:pk>/update/', views.area1_update, name='area1_update'),
    path('area1/<int:pk>/delete/', views.area1_delete, name='area1_delete'),
    
    # Area-2 & 3 Operations
    path('area23/', views.area23_list, name='area23_list'),
    path('area23/create/', views.area23_create, name='area23_create'),
    path('area23/<int:pk>/', views.area23_detail, name='area23_detail'),
    path('area23/<int:pk>/update/', views.area23_update, name='area23_update'),
    path('area23/<int:pk>/delete/', views.area23_delete, name='area23_delete'),
] 