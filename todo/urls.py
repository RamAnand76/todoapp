from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('tasks/', views.task_list, name='task_list'),  # Add a trailing slash '/'
    path('create/', views.task_create, name='task_create'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),    
    path('remove.<int:task_id>/', views.task_remove,name='task_remove'),
    path('tasks/complete/<int:task_id>/', views.task_complete, name='task_complete'),
    path('logout/', auth_views.LoginView.as_view(template_name='login.html'), name='logout'),
    path('accounts/profile/', views.redirect_to_task_list, name='profile'),

]
