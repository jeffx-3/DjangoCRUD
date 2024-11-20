from django.shortcuts import render, redirect,get_object_or_404

from .models import Item
from .forms import ItemForm

#this is just for learning django CRUD,it's really cool

#CREATE VIEW
def create_item(request):
    if request.method == 'POST':
        form =ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()        
    return render(request, 'create_item.html', {'form': form})


#READ VIEW

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


#UPDATE VIEW

def update_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)  # Define form for GET requests
    
    return render(request, 'update_item.html', {'form': form})


#DELETE VIEW

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'delete_item.html', {'item':item})