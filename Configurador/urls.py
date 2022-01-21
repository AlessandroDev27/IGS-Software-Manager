from django.contrib import admin
from django.urls import path, include
from API.viewset import EmployeeViewset
from rest_framework import routers

#Endpoint routes
# '',admin.site.urls = For the admin panel to be as first
router = routers.DefaultRouter()
router.register(r'Employees', EmployeeViewset )

urlpatterns = [
    path('', admin.site.urls),
    path('Employees/', include(router.urls))
]

