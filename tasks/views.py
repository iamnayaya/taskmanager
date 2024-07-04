from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

@login_required
def api_task_list(request):
    status = request.GET.get('status')
    if status:
        tasks = Task.objects.filter(status=status)
    else:
        tasks = Task.objects.all()
    tasks_data = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'due_date': task.due_date,
            'category': task.category,
            'assigned_to': task.assigned_to.username,
        } for task in tasks
    ]
    return JsonResponse({'tasks': tasks_data})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_progress_tasks'] = Task.objects.filter(status='in_progress')
        context['completed_tasks'] = Task.objects.filter(status='completed')
        context['overdue_tasks'] = Task.objects.filter(status='overdue')
        context['form'] = TaskForm()
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def dashboard(request):
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    in_progress_tasks = Task.objects.filter(status='In Progress').count()
    overdue_tasks = Task.objects.filter(status='Overdue').count()
    recent_activities = []  # Replace with your logic to fetch recent activities

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'overdue_tasks': overdue_tasks,
        'recent_activities': recent_activities,
    }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def calendar(request):
    return render(request, 'tasks/calendar.html')

@login_required
def members(request):
    members = User.objects.all()
    return render(request, 'tasks/members.html', {'members': members})
