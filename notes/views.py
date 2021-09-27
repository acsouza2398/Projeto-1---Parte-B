from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title = title, content = content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/note.html', {'notes': all_notes})

def delete(request):
    id = request.POST.get('id')
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('index')

def edit(request, id):
    print("----- REQUEST -----")
    print(request)
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    note = Note.objects.filter(id=id)
    

    note.update(title=title, content=content)
    
    return redirect('index')