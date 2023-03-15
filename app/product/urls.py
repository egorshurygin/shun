from django.urls import path, include
from app.product.views import *

urlpatterns = [
    path('device', GetListAllDeviceSignals.as_view()),
    path('telegram', GetListAllTelegramUsers.as_view()),
    path('create/DisplayCode', CreateDisplayCode.as_view()),
]
