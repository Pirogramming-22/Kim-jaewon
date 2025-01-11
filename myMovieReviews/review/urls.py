from django.urls import path
from .views import *


app_name = 'review'

urlpatterns = [
    path('<int:pk>/', review_detail, name='review_detail'),  # 리뷰 디테일 페이지
    path('<int:pk>/update/', review_update, name='review_update'),  # 리뷰 수정
    path('<int:pk>/delete/', review_delete, name='review_delete'),  # 리뷰 삭제
]