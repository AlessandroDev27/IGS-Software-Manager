from django.contrib import admin
from Employee_Registration.models import Employee



#list_diplay= List all fields on display
#list_diplay_links = click on the information
#search_fields = To show selected information
class Employees(admin.ModelAdmin):
    list_diplay = ('id', 'nome', 'email')
    list_diplay_links =('id', 'nome')
    search_fields =['nome']

admin.site.register(Employee, Employees) 


