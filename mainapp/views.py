from django.shortcuts import render
from .models import ProductCategory


def main(request):
    return render(request, 'mainapp/index.html')
    
def products(request, pk=None):
    categories_list = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context= {'categories': categories_list })

def contacts(request):
    return render(request, 'mainapp/contacts.html')
