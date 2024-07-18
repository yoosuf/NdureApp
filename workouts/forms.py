from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import WorkoutLog, UserPackage

User = get_user_model()

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['workout_types', 'date', 'duration', 'notes', 'trainer', 'user_package']
        widgets = {
            'workout_types': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(WorkoutLogForm, self).__init__(*args, **kwargs)
        
        # Filter customers
        try:
            customer_group = Group.objects.get(name='Customer')
            self.fields['customer'].queryset = User.objects.filter(groups=customer_group)
        except Group.DoesNotExist:
            self.fields['customer'].queryset = User.objects.none()
        
        # Filter trainers
        try:
            trainer_group = Group.objects.get(name='Trainer')
            self.fields['trainer'].queryset = User.objects.filter(groups=trainer_group)
        except Group.DoesNotExist:
            self.fields['trainer'].queryset = User.objects.none()

class UserPackageForm(forms.ModelForm):
    class Meta:
        model = UserPackage
        fields = ['package', 'start_date', 'end_date']
