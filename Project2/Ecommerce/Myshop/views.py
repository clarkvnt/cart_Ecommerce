from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.db import connection


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 6) 
    page_number = request.GET.get('page')
    try:
        products_page = paginator.page(page_number)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    cart = Cart(request) 

    return render(request, 'product_list.html', {
        'category': category,
        'categories': categories,
        'products_page': products_page,
        'cart': cart, 
    })


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)  
    return render(request, 'product_detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart, 
    })


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('Myshop:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('Myshop:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    cart_items = []  # Initialize an empty list to hold cart items
    total_cart_price = 0.0  # Initialize total price

    if cart:  # Check if the cart is not empty
        for item in cart:
            if item.get('product'):  # Use .get() to avoid KeyError
                cart_item = {
                    'product': item['product'],
                    'quantity': item['quantity'],
                    'total_price': float(item['total_price']),
                    'update_quantity_form': CartAddProductForm(
                        initial={'quantity': item['quantity'], 'update': True}
                    ),
                }
                cart_items.append(cart_item)
        total_cart_price = float(cart.get_total_price()) 

    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,
        'cart': cart, 
    })


def product_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            available=True
        )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        try:
            results_page = paginator.page(page_number)
        except PageNotAnInteger:
            results_page = paginator.page(1)
        except EmptyPage:
            results_page = paginator.page(paginator.num_pages)
    else:
        results_page = Paginator([], 6).page(1)
    categories = Category.objects.all()
    cart = Cart(request)
    return render(request, 'product_list.html', {
        'query': query,
        'products_page': results_page,
        'categories': categories,
        'cart': cart,
    })


def danger(request):
    return render(request, 'danger.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('Myshop:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('Myshop:login')