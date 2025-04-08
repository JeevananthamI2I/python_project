from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecomm_app/shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ecomm_app/shop/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'ecomm_app/shop/product_list.html', {'category': categories})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new category to the database
            return redirect('category_list')  # Redirect to a category list page or another page
    else:
        form = CategoryForm()  # Create a new form instance
    return render(request, 'ecomm_app/shop/add_category.html', {'form': form})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'ecomm_app/shop/add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'ecomm_app/shop/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'ecomm_app/shop/delete_product.html', {'product': product})