from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    insert = {'insert_me':"To Index from Views"}
    return render(request,'index.html',context=insert)

def help(request):
    help_dict = {'help_me':"To Help From views"}
    return render(request,'help.html',context=help_dict)