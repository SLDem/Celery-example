from celery import shared_task


@shared_task()
def create_order_task():
    from django.utils.crypto import get_random_string

    from random import choice

    from orders.models import Order
    from authentication.models import User

    user_pks = User.objects.values_list('pk', flat=True)
    random_pk = choice(user_pks)
    random_employee = User.objects.get(pk=random_pk)

    orders_count = Order.objects.all().count()
    name = "Order #{}".format(orders_count)
    description = get_random_string(length=32)

    Order.objects.create(
        name=name,
        description=description,
        employee=random_employee
    )

    print("Order created successfully!")
