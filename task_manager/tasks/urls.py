from django.urls import path
from task_manager.tasks import views


app_name = "tasks"


urlpatterns = [
    path('', views.TasksListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.TaskDetailsView.as_view(), name='details'),
]
