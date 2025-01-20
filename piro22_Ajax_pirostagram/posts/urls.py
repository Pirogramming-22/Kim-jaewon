from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_id>/', views.post_detail, name='post_detail'),  
    path('<int:post_id>/toggle-like/', views.toggle_like, name='toggle_like'),
    path('<int:post_id>/add-comment/', views.add_comment, name='add_comment'),
    path('<int:post_id>/delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),    
]
