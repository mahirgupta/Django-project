from django.shortcuts import redirect, render 
from django.http import HttpResponse
from django.template import loader
from.models import item
from .forms import ItemForm
# Create your views here.

def index(request):
    item_list = item.objects.all()
    template = loader.get_template('index.html')
    context={
        'item_list':item_list,
    }

    return HttpResponse(template.render(context,request))

def detail(request ,item_id):
    Item = item.objects.get(pk=item_id)
    context={
        'Item':Item,
    }
    return render(request,'detail.html',context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.instance.user_name = request.user
        form.save()
        return redirect('index')

    return render(request,'create_item.html',{'form':form})


def update(request , id):
    Item = item.objects.get(pk=id)
    form= ItemForm(request.POST or None ,instance=Item)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'create_item.html',{'form':form, 'Item':Item})


def delete(request , id):
    Item = item.objects.get(pk=id)

    if request.method=='POST':
        Item.delete()
        return redirect('index')
    
    return render(request, 'delete.html',{'Item':Item})

     

