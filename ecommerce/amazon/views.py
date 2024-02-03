from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.shortcuts import render, get_object_or_404

def product(request):
    query = request.GET.get('search', '') 
    
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()

    context = {'products': products, 'search_value': query}
    return render(request, 'pages/product.html', context)

def add(request):
    if(request.method=="POST"):
        Product.objects.create(title=request.POST['name'],
                                category=request.POST['category'],
                                price=request.POST['price'],
                                image=request.POST['image']
                                )    
        return redirect('product') 
    return render(request, 'pages/add.html')


def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)
    product_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def productDetail(request, productID):
    product = next((p for p in Product.objects.all() if p.id == productID), None)
    context = {'product': product}
    if product:
        return render(request, 'pages/productDetail.html', context)
    return HttpResponse('<span style="color:red">Product not found</span>')

def update(request, productID):
    product = get_object_or_404(Product, id=productID)

    if request.method == 'POST':
        product.title = request.POST['name']
        product.category = request.POST['category']
        product.price = request.POST['price']
        product.image = request.POST['image']
        product.save()

        return redirect('productDetail', productID=product.id)
    context = {'product': product}
    return render(request, 'pages/update.html', context)

def category(request):
    context = {'products': Product.objects.all()}
    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')
