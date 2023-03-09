from django.urls import path, include
from app.product.views import *

urlpatterns = [
    path('list/all/points', GetListAllPoints.as_view()),
    path('list/all/display_codes', GetListAllDisplayCodeProduct.as_view()),
    path('create/DisplayCode', CreateDisplayCode.as_view()),
]