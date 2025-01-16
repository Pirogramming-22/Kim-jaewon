from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('toggle_star/<int:pk>/', views.toggle_star, name='toggle_star'),
    path('update_interest/<int:pk>/<str:action>/', views.update_interest, name='update_interest'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('<int:pk>/update/', views.idea_update, name='idea_update'),
]
