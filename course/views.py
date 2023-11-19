from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from course.models import Course
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
#from .choices import counties_choices,price_choices,difficulty_rating_choices


# Create your views here.
def index(request):
    courses = Course.objects.order_by('-start_date').filter(is_published=True)

    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)

    context = {
        'courses': paged_courses
    }


    return render(request, 'courses/courses.html',context)

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    context={
        'course':course
    }
    return render(request, 'courses/course.html', context)


def search(request):

    return render(request, 'courses/search.html')