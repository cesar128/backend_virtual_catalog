# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Item, ItemPicture, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'show',
        'picture',
        'price',
        'category',
    )
    list_filter = ('show', 'category')
    search_fields = ('name',)


@admin.register(ItemPicture)
class ItemPictureAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
