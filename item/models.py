from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Category name'
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name='items'
    )
    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='item_images', blank=True, null=True
    )
    price = models.FloatField()
    is_sold = models.BooleanField(
        default=False
    )
    created_by = models.ForeignKey(
        to=User, related_name='items', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)