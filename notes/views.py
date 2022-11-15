from django.shortcuts import render

from .models import Notes

#we are quering for all notes and send them to the template
# this way when the template is rendered all the information coming directly
# from the database will be available
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes': all_notes})

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_detail.html',{'note': note})