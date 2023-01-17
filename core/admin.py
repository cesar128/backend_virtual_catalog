# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Item, ItemPicture


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'show', 'piture')
    list_filter = ('show',)
    search_fields = ('name',)


@admin.register(ItemPicture)
class ItemPictureAdmin(admin.ModelAdmin):
    list_display = ('id',)
