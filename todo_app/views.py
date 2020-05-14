import logging
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from todo_app.forms import TodoAppAddForm, TodoAppUpdateForm, TodoAppDeleteForm
from todo_app.models import TodoList

log = logging.getLogger(__name__)


@login_required
def todo_app_index(request):
    todo_list = TodoList.objects.all().order_by("created_timestamp")[:100]
    return render(request, 'todo_app_index.html', {'todo_list': todo_list})


@login_required
def todo_app_add(request):

    if request.method == 'POST':
        form = TodoAppAddForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('todo_app_display_page', todo_id=form.instance.id)
    else:
        form = TodoAppAddForm()

    return render(request, 'todo_app_add.html', {'form': form})


@login_required
def todo_app_display(request, todo_id):
    try:
        todo_obj = TodoList.objects.get(id=todo_id)
    except TodoList.DoesNotExist:
        return redirect('todo_app_index_page')

    return render(request, 'todo_app_display.html', {'todo_obj': todo_obj})


@login_required
def todo_app_update(request, todo_id):
    try:
        todo_obj = TodoList.objects.get(id=todo_id)
    except TodoList.DoesNotExist:
        return redirect('todo_app_index_page')

    if request.method == 'POST':
        form = TodoAppUpdateForm(request.POST, instance=todo_obj)
        if form.is_valid():
            if form.instance.completed_timestamp is None and \
                    form.instance.completed_flag is True:
                form.instance.completed_timestamp = datetime.now()
            form.save()
            return redirect('todo_app_display_page', todo_id=form.instance.id)
    else:
        form = TodoAppUpdateForm(instance=todo_obj)

    return render(request, 'todo_app_update.html', {'form': form,
                                                    'todo_id': todo_id})


@login_required
def todo_app_delete(request, todo_id):
    try:
        todo_obj = TodoList.objects.get(id=todo_id)
    except TodoList.DoesNotExist:
        return redirect('todo_app_index_page')

    if request.method == 'POST':
        form = TodoAppDeleteForm(request.POST)
        if form.is_valid():
            confirm = form.cleaned_data['confirm']
            if confirm is True:
                todo_obj.delete()
            return redirect('todo_app_index_page')
    else:
        form = TodoAppDeleteForm()

    return render(request, 'todo_app_delete.html', {'form': form,
                                                    'todo_id': todo_id })
