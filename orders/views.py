from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .models import Order, OrderItem

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Get or create an order in the session
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.filter(id=order_id, is_completed=False).first()
        if not order:
            order = Order.objects.create(user=request.user)
            request.session['order_id'] = order.id
    else:
        order = Order.objects.create(user=request.user)
        request.session['order_id'] = order.id
    
    # Add the book to the order
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        book=book,
        defaults={'quantity': 1}
    )
    
    # If the item already exists, increase the quantity
    if not created:
        order_item.quantity += 1
        order_item.save()
    
    return redirect('cart')

@login_required
def cart(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.filter(id=order_id, is_completed=False).first()
        if order:
            return render(request, 'orders/cart.html', {'order': order})
    
    # Empty cart
    return render(request, 'orders/cart.html', {'order': None})

@login_required
def confirm_order(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.filter(id=order_id, is_completed=False).first()
        if order:
            # Redirect to payment page
            return redirect('payment')
    
    return redirect('book_list')

@login_required
def payment(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.filter(id=order_id, is_completed=False).first()
        if order:
            if request.method == 'POST':
                # Mark the order as completed
                order.is_completed = True
                order.save()
                
                # Clear the order from the session
                del request.session['order_id']
                
                return redirect('book_list')
            
            return render(request, 'orders/payment.html', {'order': order})
    
    return redirect('book_list')