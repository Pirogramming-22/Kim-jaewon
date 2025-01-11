from django.urls import path
from .views import *


app_name = 'movie'

urlpatterns = [
    path('', review_list, name='review_list'),  # 리뷰 리스트 페이지
    path('reviews/create/', review_create, name='review_create'),  # 리뷰 작성
]