from rest_framework.viewsets import ModelViewSet
from Employee_Registration.models import Employee
from API.serializer import EmployeeSerializer


#queryset = Select all objects in the model

class EmployeeViewset(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer