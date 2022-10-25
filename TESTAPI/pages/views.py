from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt            # models için
from rest_framework.parsers import JSONParser            # models için
from django.http.response import JsonResponse            # models için

from pages.models import Departments,Employees            # models için

from pages.serializers import DeparmentsSerializer,EmployeeSerializer            # models için


# Create your views here.

# http://127.0.0.1:8000

def index(request):                                         #urls'de tanımlanan pathlerin html dosyalarıyla bağlantısı sağlandı.
    
    return render(request, 'pages/index.html')

def about(request):                                         # daha sonra templates/pages klasörü altına geçilip ilgili .html dosyaları oluşturuldu    
    
    return render(request, 'pages/about.html')



@csrf_exempt
def departmentsApi(request,id=0):       # Departments modeli için API metotları
    
    if request.method == 'GET':                                 # Bütün kayıtlar json formatında return edilir.(serializer kullanılarak) 
        departments = Departments.objects.all()
        departments_serializer=DeparmentsSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    elif request.method == 'POST':                              # Departments table'ına yeni bilgiler INSERT etmek için kullanılır.
        department_data=JSONParser().parse(request)
        departments_serializer=DeparmentsSerializer(data=department_data)       # json dosyası parse edilir ve serializer kullanılarak modele çevrilir.
        if departments_serializer.is_valid():                                   # model doğruysa database'e kaydedilir ve başarılı mesajı gönderilir.
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
        
    elif request.method=='PUT':                                            # Verilen kaydı güncellemek (UPDATE) için kullanılır.         
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])            # DepartmentID kullanılarak varolan kayıt seçilir.
        departments_serializer=DeparmentsSerializer(department,data=department_data)            # veriler birleştirilir (mapping)
        if departments_serializer.is_valid():                    # model geçerliyse kaydedilir.
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':                                  # Seçilen veriyi siler. (DELETE)
        department=Departments.object.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted successfully",safe=False)
    
    
@csrf_exempt
def employeeApi(request,id=0):     # Employees modeli için API metotları
    
    if request.method == 'GET':                                 # Bütün kayıtlar json formatında return edilir.(serializer kullanılarak) 
        employee = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
        
    elif request.method == 'POST':                              # Employees table'ına yeni bilgiler INSERT etmek için kullanılır.
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)       # json dosyası parse edilir ve serializer kullanılarak modele çevrilir.
        if employees_serializer.is_valid():                                   # model doğruysa database'e kaydedilir ve başarılı mesajı gönderilir.
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
            
    elif request.method=='PUT':                                            # Verilen kaydı güncellemek (UPDATE) için kullanılır.         
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeetId=employee_data['EmployeeId'])            # EmployeesID kullanılarak varolan kayıt seçilir.
        employees_serializer=EmployeeSerializer(employee,data=employee_data)            # veriler birleştirilir (mapping)
        if employees_serializer.is_valid():                    # model geçerliyse kaydedilir.
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
        
    elif request.method=='DELETE':                                  # Seçilen veriyi siler. (DELETE)
        employee=Employees.object.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted successfully",safe=False)
