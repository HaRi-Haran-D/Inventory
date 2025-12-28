from django.shortcuts import render
from .forms import ItemForm
from .models import Items

# Create your views here.
def home(request):
    return render(request, 'inventapp/home.html')

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm()
    return render(request, 'inventapp/add_item.html', {'form': form})


def list_items(request):
    items = Items.objects.all()
    return render(request, 'inventapp/list_items.html', {'items': items})


def update_item(request, item_id):
    items = Items.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm(instance=items)
    return render(request, 'inventapp/update_item.html', {'form': form})
