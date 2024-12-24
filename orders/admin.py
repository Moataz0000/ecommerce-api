from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'product', 'quantity', 'status', 'created')
    list_filter = ('status', 'created')
    search_fields = ('order_id', 'user__email', 'product__name')
    ordering = ('-created',)
    readonly_fields = ('order_id', 'created')

    fieldsets = (
        (None, {
            'fields': ('order_id', 'user', 'product', 'quantity', 'status', 'created')
        }),
    )
