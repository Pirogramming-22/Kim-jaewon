from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Idea, IdeaStar
from devtool.models import DevTool
from .forms import IdeaForm
from django.db.models import Case, When, BooleanField

def idea_list(request):
    ideas = Idea.objects.all()

    #정렬
    sort_option = request.GET.get('sort', 'latest')
    if sort_option == 'latest':
        ideas = ideas.order_by('-id')  # 최신순 (id 역순)
    elif sort_option == 'oldest':
        ideas = ideas.order_by('id')  # 등록순 (id 순서)
    elif sort_option == 'name':
        ideas = ideas.order_by('title')  # 이름순
    elif sort_option == 'star':
        ideas = ideas.annotate(
            is_starred=Case(
                When(star__is_starred=True, then=True),
                default=False,
                output_field=BooleanField(),
            )
        ).order_by('-is_starred', '-id')  # 찜 여부 우선, 그다음 최신순


    paginator = Paginator(ideas, 4)  # 한 페이지에 4개의 아이템
    page_number = request.GET.get('page')  # 현재 페이지 번호
    page_obj = paginator.get_page(page_number)  # 해당 페이지의 아이템 가져오기
    return render(request, 'idea/idea_list.html', {'page_obj': page_obj, 'sort_option': sort_option})

def toggle_star(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)
        star, created = IdeaStar.objects.get_or_create(idea=idea)
        star.is_starred = not star.is_starred
        star.save()
        return JsonResponse({"is_starred": star.is_starred})
    return JsonResponse({"error": "Invalid request method."}, status=400)

def update_interest(request, pk, action):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)
        if action == 'increment':
            idea.interest += 1
        elif action == 'decrement' and idea.interest > 0:
            idea.interest -= 1
        idea.save()
        return JsonResponse({"success": True, "interest": idea.interest})
    return JsonResponse({"success": False, "error": "Invalid request method."}, status=400)

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            
            devtools = request.POST.getlist('devtools')
            idea.devtools.set(devtools)
            return redirect('idea_detail', pk=idea.pk)
    else: #GET이면
        form = IdeaForm()
    devtools = DevTool.objects.all()  
    return render(request, 'idea/idea_create.html', {'form': form, 'devtools': devtools})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'idea/idea_detail.html', {'idea': idea})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'idea_list')

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'idea/idea_update.html', {'form': form, 'idea': idea})

