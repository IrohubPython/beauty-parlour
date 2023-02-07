from django.urls import path
from . import views

urlpatterns = [
    path('adminindex/', views.adminindex, name='adminindex'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('add_branches/', views.add_branches, name='add_branches'),
    path('view_branches/', views.view_branches, name='view_branches'),
    path('b_edit/<int:eid>/',views.b_edit,name='b_edit'),
    path('edit_branches/<int:id>/',views.edit_branches,name='edit_branches'),
    path('delete_branches/<int:id>/',views.delete_branches,name='delete_branches'),
    path('add_services/', views.add_services, name='add_services'),
    path('view_services/', views.view_services, name='view_services'),
    path('service_data',views.service_data,name='service_data'),
    path('edit_service/<int:id>/',views.edit_service,name='edit_service'),
    path('edit_s/<int:eid>/',views.edit_s,name='edit_s'),
    path('delete_s/<int:id>/',views.delete_s,name='delete_s'),
    path('view_users/', views.view_users, name='view_users'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('view_messages/', views.view_messages, name='view_messages'),



]