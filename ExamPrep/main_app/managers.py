from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(
            orders_count=Count('orders')
        ).filter(
            orders_count__gt=2,
        ).order_by(
            '-orders_count'
        )
