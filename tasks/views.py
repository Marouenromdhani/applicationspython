from django.shortcuts import render, redirect
from django.http import HttpResponse

from tasks.models import Collection


# Create your views here.
def index(request):
    context = {}


    context["collections"] = Collection.objects.order_by("name")
    return render(request, 'tasks/index.html', context={})

def add_collection(request):
 collection_name = request.POST.get("collection-name")
 Collection.objects.create(name=collection_name)
 return redirect('home')

