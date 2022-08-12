from django.shortcuts import render, redirect
import total as total
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='/users/sign_in')
def home(request):
    search = request.GET.get('input')
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    product_id = request.GET.get('product')

    if product_id:
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(
                customer=request.user,
                product=product,
                quantity=1
            )
            cart_item.save()
            return redirect('shop:home')
        for item in cart_item:
            item.quantity += 1
            item.save()


    products = Product.objects.all()
    products = products.filter(
        Q(title__icontains=search) | Q(description__icontains=search)
    ) if search else products
    slides = Slide.objects.all()
    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products
    return render(request, 'home.html', {'products': products, 'slides': slides})


def cart(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(
        request,
        'cart.html',
        {'cart_items': cart_items,
         'total_price': total_price,
         'total_quantity': total_quantity}
    )


def delete_cart_item(request, pk):
    CartItem.objects.get(pk=pk).delete()
    return redirect('shop:cart')


def edit_cart_items(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    action = request.GET.get('action')

    if action == 'decrement' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('shop:cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('shop:cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:cart')
