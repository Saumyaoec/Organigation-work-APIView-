from django.urls import path
from modules.adminDashboardApp.views import EmployeeProfileList, EmployeeProfileDetail
from modules.adminDashboardApp.views import CompaneyCreateList, CompanyRetrieveUpdateDestroy
from modules.adminDashboardApp.views import DepartmentCreateList, DepartmentRetrieveUpdateDestroy
from modules.adminDashboardApp.views import JoinLetterAPIView, ConvertPdfAPIView
app_name='adminDashboardApp'
urlpatterns = [
    path('employee/create_list/', EmployeeProfileList.as_view(), name='create_list'),
    path('employee/retrieve_update_estroy/<slug:slug>/', EmployeeProfileDetail.as_view(), name='retrieve_update_estroy'),
    path('company/create_list/', CompaneyCreateList.as_view()),
    path('company/retrieve_update_destroy/<slug:slug>/', CompanyRetrieveUpdateDestroy.as_view()),
    path('department/create_list/', DepartmentCreateList.as_view(), name='department_create_list'),
    path('department/retrieve_update_destroy/<slug:slug>/', DepartmentRetrieveUpdateDestroy.as_view(), name='department_retrieve_update_destroy'),
    path('join-letter/', JoinLetterAPIView.as_view(), name='join_letter'),
    path('convert_pdf/', ConvertPdfAPIView.as_view(), name='convert_pdf')
]