from django.shortcuts import render, redirect, get_object_or_404
from .models import DevTool
from .forms import DevToolForm

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'devtool/devtool_list.html', {'devtools': devtools})

def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm()
    return render(request, 'devtool/devtool_create.html', {'form': form})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = devtool.ideas.all()  # 역참조로 연결된 아이디어 목록 가져오기
    #idea/model.py에서 related_name을 지정해놨기 때문에 ideas.all로 가능
    return render(request, 'devtool/devtool_detail.html', {'devtool': devtool, 'ideas': ideas})

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtool_list')
    
def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'devtool/devtool_update.html', {'form': form, 'devtool': devtool})
