from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'CDN.html')

def Local(request):
    return render(request,'Local.html')