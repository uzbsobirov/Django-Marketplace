from django.urls import path
from item.views import ItemDetailView

app_name = 'item'

urlpatterns = [
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='item_detail')
]