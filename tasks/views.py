from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.views.decorators.http import require_POST

def index(request):
    tasks = Task.objects.all().order_by('id')# Sort by ID
    return render(request, 'tasks/index.html', {'tasks': tasks})

#Adds task to database. Title is required but desc isnt only title is needed to add task
@require_POST
def add_task(request):
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    if title:
        Task.objects.create(title=title, description=description)
    return redirect('index')

#Changes task to completed or back to complete in database
@require_POST
def toggle_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

#Deletes task from the database
@require_POST
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')

#gets title and description from edit inputs and changes the info based on inputs
def edit_task(request, task_id):
    description = request.POST.get('description', '')
    title = request.POST.get('title', '')
    if title:
        task = Task.objects.get(pk=task_id)
        task.title = title
        task.save()
    if description:
        task = Task.objects.get(pk=task_id)
        task.description = description
        task.save()

    return redirect('index')




