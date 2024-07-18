from django.urls import path
from .views import workout_log_list, add_workout_log, edit_workout_log, user_package_list, add_user_package, edit_user_package

urlpatterns = [
    path('logs/', workout_log_list, name='workout_log_list'),
    path('logs/add/', add_workout_log, name='add_workout_log'),
    path('logs/edit/<int:pk>/', edit_workout_log, name='edit_workout_log'),
    path('packages/', user_package_list, name='user_package_list'),
    path('packages/add/', add_user_package, name='add_user_package'),
    path('packages/edit/<int:pk>/', edit_user_package, name='edit_user_package'),
]