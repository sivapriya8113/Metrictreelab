from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import employeeserializer
from .models import Employee

# Create your views here.
'''@api_view(['Get'])
def api_overview(request):
    api_urls={
        'List': '/product-list/',
        'Detail view': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }
    return Response(api_urls)  '''


#list
@api_view(['Get'])
def showall(request):
    employees = Employee.objects.all()
    serializer = employeeserializer(employees, many=True)
    return Response(serializer.data)

#single product

@api_view(['Get'])
def Viewemployee(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = employeeserializer(emp, many=False)
    return Response(serializer.data)

#create product
@api_view(['Post'])
def createemployee(request):
    serializer = employeeserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['Post'])
def Updateemployee(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = employeeserializer(instance=emp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#delete
@api_view(['Get'])
def Deleteemployee(request,pk):
    employees = Employee.objects.get(id=pk)
    employees.delete()

    return Response("Items Deleted Successfully")

