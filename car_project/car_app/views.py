from .forms import UPCars
from .models import Cars,Category
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import  Paginator,InvalidPage,EmptyPage


# Create your views here.
def home(request,c_slug=None):
    c_page=None
    cars_list=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        cars_list=Cars.objects.all().filter(category=c_page)
    else :

        cars_list=Cars.objects.all()

    paginator = Paginator(cars_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        cars = paginator.page(page)
    except (EmptyPage, InvalidPage):
        cars = paginator.page(paginator.num_pages)


    return render(request,'home.html',{'cars_list':cars,'category':c_page})

def car_detail(request,c_slug,o_slug):
    try:
        car=Cars.objects.get(category__slug=c_slug,slug=o_slug)
    except Exception as e:
        raise e
    return  render(request,'product.html',dict(car=car))

def update(request,c_slug,o_slug):
    car=Cars.objects.get(category__slug=c_slug,slug=o_slug)
    form=UPCars(request.POST or None,request.FILES,instance=car)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'car':car})

def delete(request,c_slug,o_slug):
    car=Cars.objects.get(category__slug=c_slug,slug=o_slug)
    if request.method == 'POST':
        car.delete()
        return redirect('/')
    return render(request,'delete.html')
