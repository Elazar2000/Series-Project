from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Series
from . forms import seriesForm
# Create your views here.
def home(request):
    series = Series.objects.all()
    list = {
        'series_list': series
    }
    return render(request,'home.html',list)

def detail(request,series_id):
    series = Series.objects.get(id=series_id)
    return render(request,'detail.html',{'series':series})

def add_series(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        disc = request.POST.get('disc',)
        year = request.POST.get('Year',)
        img = request.FILES['img']
        series = Series(name=name,disc=disc,year=year,img=img)
        series.save()
    return render(request,'add.html')

def update(request,id):
    series = Series.objects.get(id=id)
    form = seriesForm(request.POST or None, request.FILES, instance=series)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'series':series})

def delete(request,id):
    if request.method == 'POST':
        series = Series.objects.get(id=id)
        series.delete()
        return redirect('/')
    return render(request,'delete.html')
