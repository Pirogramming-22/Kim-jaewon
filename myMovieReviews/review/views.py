from django.shortcuts import render, get_object_or_404, redirect
from .models import Review

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review/review_detail.html', {'review': review})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.title = request.POST.get('title')
        review.release_year = request.POST.get('release_year')
        review.director = request.POST.get('director')
        review.main_actor = request.POST.get('main_actor')
        review.genre = request.POST.get('genre')
        review.rating = request.POST.get('rating')
        review.running_time= request.POST.get('running_time')
        review.content = request.POST.get('content')
        review.save()
        return redirect('review:review_detail', pk=review.pk)
    return render(request, 'movie/review_form.html', {'action': 'update', 'review': review})

def review_delete(request, pk):
    if request.method == "POST":
        review = get_object_or_404(Review, pk=pk)
        review.delete()
    return redirect('movie:review_list')
