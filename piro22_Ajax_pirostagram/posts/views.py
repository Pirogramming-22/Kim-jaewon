from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment
import json

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post.html', context)

@csrf_exempt
def toggle_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)  # 좋아요 취소
        liked = False
    else:
        post.likes.add(user)  # 좋아요 추가
        liked = True

    return JsonResponse({'liked': liked, 'likes_count': post.likes_count})

@csrf_exempt
def add_comment(request, post_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # JSON 데이터 파싱
            content = data.get("content")
            if not content:
                return JsonResponse({"error": "Content is required."}, status=400)
            
            post = get_object_or_404(Post, id=post_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content)
            
            return JsonResponse({
                'id': comment.id,
                'user': comment.user.username,
                'content': comment.content,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=400)

    
@csrf_exempt
def delete_comment(request, post_id, comment_id):
    if request.method == "DELETE":
        try:
            comment = Comment.objects.get(id=comment_id, post_id=post_id, user=request.user)
            comment.delete()
            return JsonResponse({'deleted': True})
        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment does not exist or you do not have permission to delete it.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)