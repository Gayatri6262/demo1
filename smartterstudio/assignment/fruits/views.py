from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  Fruit



# Create your views here.
def get_fruits(request):
    data=Fruit.objects.all().order_by('-created_at')

    return render(request, 'index.html',{'data':data})


def save_fruits(request):
    fruit_name = request.POST.get('fruit_name')
    fruit_price = request.POST.get('fruit_price')
    Fruit.objects.create(name=fruit_name,price=fruit_price)
    return redirect('get_fruits')


def update_fruits(request):
    id=request.GET.get('id')
    data=Fruit.objects.get(id=id)
    return render(request,'update.html',{'data':data})

def delete_fruits(request):
    id=request.GET.get('id')
    Fruit.objects.get(id=id).delete()
    return redirect('get_fruits')
def edited_fruits(request):
    id=request.POST.get('ids')
    print(id)
    name=request.POST.get('fruit_name')
    print(name)
    price = request.POST.get('fruit_price')
    fruits=Fruit.objects.get(id=id)
    fruits.name=name
    fruits.price=price
    fruits.save()
    return redirect('get_fruits')
