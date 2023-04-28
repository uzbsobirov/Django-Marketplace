from django.shortcuts import render, get_object_or_404
from .models import Item
from django.views import View

class ItemDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Item, pk=pk)
        related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

        context = {
            'item': item,
            'related_items': related_items
        }

        return render(request=request, template_name='item/detail.html', context=context)