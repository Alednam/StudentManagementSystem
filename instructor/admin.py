from django.contrib import admin

# Register your models here.
from .models import Instructor

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Instructor, InstructorAdmin)