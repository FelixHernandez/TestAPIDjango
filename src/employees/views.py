from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
 
class EmployeesView(APIView):
 
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
   
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
   
   
    def get(self, request, id=None):
        if id:
            employee = Employee.objects.get(pk=id)
            serializer = EmployeeSerializer(employee)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
 
    def put(self, request, id=None):
        employee = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
 
 
    def delete(self, request, id=None):
        student = get_object_or_404(Employee, id=id)
        student.is_deleted = True
        return Response({"status": "success", "data": "student Deleted"})
   
 
class BeneficiariesView(APIView):
   
    def get(self, request, id=None):
        if id:
            beneficiary = Beneficiary.objects.get(pk=id)
            serializer = BeneficiarySerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 
        beneficiary = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(beneficiary, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
   
    def post(self, request):
        serializer = BeneficiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
   
   
    def put(self, request, id=None):
        beneficiary = Beneficiary.objects.get(pk=id)
        serializer = BeneficiarySerializer(beneficiary, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})