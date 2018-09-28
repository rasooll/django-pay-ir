from .urls import urlpatterns
from django.urls import path, include

urlpatterns += [path('/payment/', include('pay_ir.urls'))]