from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# from .tasks import order_created
from django.core.mail import send_mail
from django.urls import reverse


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            # order_created.delay(order.id)
            message = f'Dear {order.first_name}, \nYou have successfully placed an order.\nYour order ID is {order.id}.'
            send_mail('Order', message, 'avc9999@outlook.com',\
                      [form.cleaned_data['email']], fail_silently=False)
            # return render(request,
            #               'orders/order/created.html',
            #               {'order': order})
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
