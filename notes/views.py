from django.shortcuts import render
from django.http import Http404

from .models import Notes

#we are quering for all notes and send them to the template
# this way when the template is rendered all the information coming directly
# from the database will be available
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes': all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html',{'note': note})