from django.contrib import admin
from app.product.models import TelegramUsers, DeviceSignals


admin.site.register(TelegramUsers)
admin.site.register(DeviceSignals)
