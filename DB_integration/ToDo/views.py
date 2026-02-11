from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoList, Task
from django.shortcuts import redirect
from django.views import View


class HomeView(ListView):
    model = TodoList
    template_name = 'home.html'
    context_object_name = 'lists'


class AddListView(CreateView):
    model = TodoList
    fields = ['name']
    success_url = reverse_lazy('home')


class AddTaskView(CreateView):
    model = Task
    fields = ['todo_list', 'title']
    success_url = reverse_lazy('home')


class DeleteTaskView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('home')


class DeleteListView(View):
    def get(self, request, pk):
        todo_list = TodoList.objects.get(id=pk)
        todo_list.delete()
        return redirect('home')
