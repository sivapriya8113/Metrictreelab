from django.urls import path

from . import views

urlpatterns=[
    #path('',views.api_overview, name='api_overview'),
    path('employee-list/', views.showall, name='employee-list'),
    path('employee-detail/<int:pk>/', views.Viewemployee, name='employee-details'),
    path('employee-create/', views.createemployee, name='employee-create'),
    path('employee-update/<int:pk>/', views.Updateemployee, name='employee-update'),
    path('employee-delete/<int:pk>/', views.Deleteemployee, name='employee-delete'),

]