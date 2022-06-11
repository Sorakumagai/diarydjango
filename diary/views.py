from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def index(request):
    all_data = Note.objects.all()
    context = {
        'title': '一覧画面',
        'all_data': all_data,
    }
    return render(request, 'diary/index.html', context)

def new(request):
    noteform = NoteForm()
    context = {
        'title': '新規作成画面',
        'noteform': noteform,
    }
    return render(request, 'diary/new.html', context)

def create(request):
    if request.method == 'POST':
        new_data = NoteForm(request.POST)
        if new_data.is_valid():
            new_data.save()
    return redirect('diary:index')

def detail(request, id):
    data = get_object_or_404(Note, pk=id)
    content = {
        'title': '詳細画面',
        'data': data,
    }
    return render(request, 'diary/detail.html', content)

def edit(request, id):
    data = get_object_or_404(Note, pk=id)
    noteform = NoteForm(instance=data)
    context = {
        'title': '編集画面',
        'data': data,
        'noteform': noteform,
    }
    return render(request, 'diary/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        data = get_object_or_404(Note, pk=id)
        update_data = NoteForm(request.POST, instance=data)
        if update_data.is_valid():
            update_data.save()
    return redirect('diary:index')

def delete(request, id):
    delete_data = get_object_or_404(Note, pk=id)
    delete_data.delete()
    return redirect('diary:index')

