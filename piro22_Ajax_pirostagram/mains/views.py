from django.shortcuts import render
from posts.models import Post

def main(request):
    posts = Post.objects.all()  # 모든 Post 데이터를 가져옴
    return render(request, 'mains/index.html', {'posts': posts})
