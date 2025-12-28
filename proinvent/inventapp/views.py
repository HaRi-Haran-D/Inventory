from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ItemForm
from .models import Items

# Create your views here.
def home(request):
    items = Items.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:
        return render(request, 'inventapp/home.html',{'item': items})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully.")
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'inventapp/add_item.html', {'form': form})


def list_items(request):
    items = Items.objects.all()
    return render(request, 'inventapp/list_items.html', {'item': items})


def update_item(request, item_id):
    items = Items.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully.")
            return redirect('list_items')
    else:
        form = ItemForm(instance=items)
    return render(request, 'inventapp/update_item.html', {'form': form, 'item': items})


def delete_item(request, item_id):
    items = Items.objects.get(id=item_id)
    if request.method == 'POST':
        items.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect('list_items')
    return render(request, 'inventapp/list_items.html', {'item': Items.objects.all()})