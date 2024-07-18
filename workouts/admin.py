from django.contrib import admin
from .models import WorkoutType, WorkoutLog, TrainingPackage, UserPackage

@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date', 'duration', 'trainer', 'user_package']
    search_fields = ['customer__username', 'workout_types__name']
    list_filter = ['date', 'workout_types']
    filter_horizontal = ('workout_types',)

@admin.register(TrainingPackage)
class TrainingPackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'sessions', 'extra_sessions']
    search_fields = ['name']

@admin.register(UserPackage)
class UserPackageAdmin(admin.ModelAdmin):
    list_display = ['customer', 'package', 'start_date', 'end_date', 'total_sessions']
    search_fields = ['customer__username', 'package__name']
    list_filter = ['start_date', 'end_date', 'package']
