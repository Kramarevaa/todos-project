from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'pages/index.html', context=context)

 
def about_index(request):
    context = {
        "message": "The men who sold the world000000000000",
        "color": "#34AB5E"
    }
    return render(request, 'pages/about_index.html', context=context)

def create_task(request):
    if request.method == 'POST':
        print(request.POST)
        new_task = Task()
        if 'title' in request.POST:
            new_task.title = request.POST['title']
        if 'description' in request.POST:
            new_task.description = request.POST['description']
        if 'priority' in request.POST:
            new_task.priority = int (request.POST['priority'])
        new_task.save()
    return redirect('index')
        
def complete_task(request, task_id):
    task = Task.objects.get(id=str(task_id))
    if task.is_complete:
        task.is_complete = False
    else:
        task.is_complete = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')




def base(request):
    context = {

    }

def text(request):
    context = {

    }