from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutLog, UserPackage
from .forms import WorkoutLogForm, UserPackageForm

@login_required
def workout_log_list(request):
    logs = WorkoutLog.objects.filter(customer=request.user)
    return render(request, 'workouts/workout_log_list.html', {'logs': logs})

@login_required
def add_workout_log(request):
    if request.method == 'POST':
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            workout_log = form.save(commit=False)
            workout_log.customer = request.user
            workout_log.save()
            form.save_m2m()  # Save the many-to-many data for the form
            return redirect('workout_log_list')
    else:
        form = WorkoutLogForm()
    return render(request, 'workouts/add_workout_log.html', {'form': form})

@login_required
def edit_workout_log(request, pk):
    workout_log = get_object_or_404(WorkoutLog, pk=pk)
    if request.method == 'POST':
        form = WorkoutLogForm(request.POST, instance=workout_log)
        if form.is_valid():
            form.save()
            return redirect('workout_log_list')
    else:
        form = WorkoutLogForm(instance=workout_log)
    return render(request, 'workouts/edit_workout_log.html', {'form': form})

@login_required
def user_package_list(request):
    packages = UserPackage.objects.filter(customer=request.user)
    return render(request, 'workouts/user_package_list.html', {'packages': packages})

@login_required
def add_user_package(request):
    if request.method == 'POST':
        form = UserPackageForm(request.POST)
        if form.is_valid():
            user_package = form.save(commit=False)
            user_package.customer = request.user
            user_package.save()
            return redirect('user_package_list')
    else:
        form = UserPackageForm()
    return render(request, 'workouts/add_user_package.html', {'form': form})

@login_required
def edit_user_package(request, pk):
    user_package = get_object_or_404(UserPackage, pk=pk)
    if request.method == 'POST':
        form = UserPackageForm(request.POST, instance=user_package)
        if form.is_valid():
            form.save()
            return redirect('user_package_list')
    else:
        form = UserPackageForm(instance=user_package)
    return render(request, 'workouts/edit_user_package.html', {'form': form})
