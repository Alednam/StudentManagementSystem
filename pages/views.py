from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from instructor.models import Instructor


def about(request):
    instructors= Instructor.objects.order_by('-registered_date')
    # getmvp
    mvp_instructors = Instructor.objects.all().filter(is_mvp=True)

    context = {
        'instructors': instructors,
        'mvp_instructors': mvp_instructors

    }

    return render(request, 'pages/about.html', context)



