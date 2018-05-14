from django.db import models


class ItemMapper(models.Model):
    name = models.CharField(default="", max_length=255)
    notes = models.CharField(default="", max_length=1000)
    uid = models.CharField(max_length=100, primary_key=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class WarehouseItemMapper(models.Model):
    name = models.CharField(default="", max_length=255)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'WarehouseItem'
        verbose_name_plural = 'WarehouseItems'


class WarehouseMapper(models.Model):
    name = models.CharField(default="", max_length=255)
    uid = models.CharField(max_length=100, primary_key=True)
    items = models.ManyToManyField(WarehouseItemMapper)

    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
