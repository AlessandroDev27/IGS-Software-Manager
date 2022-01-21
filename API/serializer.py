from rest_framework import serializers
from Employee_Registration.models  import Employee


#fields = All fields that will be seralized
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']