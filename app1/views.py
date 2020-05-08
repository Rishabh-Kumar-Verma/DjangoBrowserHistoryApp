# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SearchField
from .models import URLbox

next=-1
# Create your views here.
def post(request):
    if request.method == 'POST':
        form = SearchField(request.POST)
        if request.POST.get("input"):
            data=URLbox(url=request.POST.get("input"))
            data.save()
            return HttpResponseRedirect('/')
    else:
        form=SearchField()

    return render(request,'index.html')

def getdata(request):
    if request.method == 'POST':
        form = SearchField(request.POST.get("input",""))
        if request.POST.get("input"):
            data=URLbox(url=request.POST.get("input",""))
            data.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        item=URLbox.objects.all()
        store=[]
        for i in range(len(item)-1,-1,-1):
            store.append(item[i].url)
        form=SearchField()
        return render(request,'index.html',{'item':store})
    else:
        form=SearchField()    
    return render(request,'index.html')

def getprev(request):
    global next
    if request.method == 'POST':
        form = SearchField(request.POST.get("input",""))
    if request.POST.get("input"):
            data=URLbox(url=request.POST.get("input",""))
            data.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        item=URLbox.objects.all()
        if next==0:
            next=0
        elif next==-1 and len(item)==0:
            return render(request,'index.html',{'holder':'no data found'})
        else:
            next-=1
        data=item[next].url
        form=SearchField()
        return render(request,'index.html',{'holder':data})
    else:
        form=SearchField()    
    return render(request,'index.html')


def getnext(request):
    global next
    if request.method == 'POST':
        form = SearchField(request.POST)
    if request.POST.get("input"):
            data=URLbox(url=request.POST['url'])
            data.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        item=URLbox.objects.all()
        if next==len(item)-1:
            next=len(item)-1
        elif next==-1 and len(item)==0:
            return render(request,'index.html',{'holder':'no data found'})
        else:
            next+=1
        data=item[next].url
        form=SearchField()
        return render(request,'index.html',{'holder':data})
    else:
        form=SearchField()    
    return render(request,'index.html')