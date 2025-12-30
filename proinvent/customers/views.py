from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'customers/base.html')

def cart(request):
    pass
    #return render(request, 'customers/cart.html')