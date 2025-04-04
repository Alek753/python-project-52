from django.urls import path
from task_manager.users import views


app_name = "users"


urlpatterns = [
    path('', views.UsersListView.as_view(), name='list'),
    path('create/', views.UserCreateView.as_view(), name='create'),
]
