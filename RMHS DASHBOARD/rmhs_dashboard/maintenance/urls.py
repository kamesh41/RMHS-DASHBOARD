from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    # Maintenance Activities
    path('', views.maintenance_list, name='list'),
    path('create/', views.maintenance_create, name='create'),
    path('<int:pk>/', views.maintenance_detail, name='detail'),
    path('<int:pk>/update/', views.maintenance_update, name='update'),
    path('<int:pk>/delete/', views.maintenance_delete, name='delete'),
    path('<int:pk>/complete/', views.maintenance_complete, name='complete'),
    
    # Spare Parts
    path('spares/', views.spare_list, name='spare_list'),
    path('spares/create/', views.spare_create, name='spare_create'),
    path('spares/<int:pk>/', views.spare_detail, name='spare_detail'),
    path('spares/<int:pk>/update/', views.spare_update, name='spare_update'),
    path('spares/<int:pk>/delete/', views.spare_delete, name='spare_delete'),
] 