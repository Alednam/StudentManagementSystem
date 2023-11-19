from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'start_date', 'instructor')
    list_display_links = ('id', 'title')
    list_filter = ('instructor',)
    list_editable = ('is_published',)
    search_fields = ('title','location', 'description', 'difficulty_rating', 'No_of_checkpoints', 'county', 'No_of_routes', 'price')
    list_per_page = 25

admin.site.register(Course, CourseAdmin)