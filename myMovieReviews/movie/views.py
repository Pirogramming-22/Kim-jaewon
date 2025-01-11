from django.shortcuts import render , redirect, get_object_or_404
from django.urls import reverse
from review.models import Review

# Create your views here.

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'movie/review_list.html', {'reviews': reviews})


def review_create(request):
    if request.method == 'POST':
        Review.objects.create(
            title=request.POST['title'],
            release_year = request.POST['release_year'],  
            director=request.POST['director'],
            main_actor=request.POST['main_actor'],
            genre=request.POST['genre'],
            rating=request.POST['rating'],
            running_time=request.POST['running_time'],
            content=request.POST['content']
        )
        return redirect(reverse('movie:review_list'))  

    return render(request, 'movie/review_form.html',{'action': 'create'})

