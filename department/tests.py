from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from department.models import Designation, Department
from django.contrib.auth.models import User
# Create your tests here.
class TestDepartmentModel(TestCase):
   

    def test_create_department_data(self):
        user = User.objects.create(username="sudan", password="sudan")
        des = Department.objects.create(
            name = "IT",
            created_by=user
        )
        
        self.assertEqual(Department.objects.count() ,1)
        self.assertEqual(Department.objects.filter(is_active=False).count(),1)
        self.assertEqual(Department.objects.filter(is_active=True).count(),0)
        self.assertEqual(des.name, "IT")

class TestDepartmentAPIView(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)
        self.dep= Department.objects.create(
            name = "IT",
            created_by=self.user,
            is_active=True
        )

    def test_department_list(self):
        url = reverse('department-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_active_department(self):
        dep = Department.objects.create(
            name = "IT",
            created_by=self.user,
        )
        url = reverse('department-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()),1)
        self.assertEqual(Department.objects.count(),2)


        
