from django.shortcuts import render
from car_app.models import Cars
from django.db.models import Q
# Create your views here.
def search_car(request):
    cars=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        cars=Cars.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'query':query,'cars':cars})
