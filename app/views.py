from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='this data is our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)
def login(request):
    d={'username':'balaji','age':24}
    return render(request,'login.html',context=d)