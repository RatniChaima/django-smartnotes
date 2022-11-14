from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',) #to display in the tible by title

admin.site.register(models.Notes, NotesAdmin)
