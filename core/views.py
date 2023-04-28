from django.shortcuts import render
from django.views import View

from item.models import Category, Item
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }

    return render(request=request, template_name='core/index.html', context=context)

def contact(request):
    return render(request, 'core/contact.html')


# class SignUp(View):
#     def get(self, request, *args, **kwargs):
#         form = SignUpForm()
#         context = {
#             'form': form
#         }
#         return render(request, template_name='core/signup.html', context=context)
#
#     def post(self, request, *args, **kwargs):
#         form = SignUpForm(request.POST)
#


def signup(request):
    form = SignUpForm()

    context = {
                'form': form
            }
    return render(request, template_name='core/signup.html', context=context)

