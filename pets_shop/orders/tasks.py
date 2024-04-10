# from celery import shared_task
# from django.core.mail import send_mail
# from .models import Order
# from celery.utils.log import get_task_logger
#
# logger = get_task_logger(__name__)
#
# @shared_task
# def order_created(order_id):
#     try:
#         order = Order.objects.get(id=order_id)
#         subject = f'Order nr. {order.id}'
#         message = f'Dear {order.first_name}, \nYou have successfully placed an order.\n' \
#                   f'Your order ID is {order.id}.'
#         mail_sent = send_mail(subject, message, 'avc9999@outlook.com', [order.email], fail_silently=False)
#
#         return mail_sent
#     except Exception as e:
#         logger.error(f'Error:{e}')
#         return False
