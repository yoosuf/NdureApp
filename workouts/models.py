from django.db import models
from django.conf import settings


class WorkoutType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TrainingPackage(models.Model):
    name = models.CharField(max_length=100)
    sessions = models.PositiveIntegerField()
    extra_sessions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UserPackage(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey(TrainingPackage, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    @property
    def total_sessions(self):
        return self.package.sessions + self.package.extra_sessions

    def __str__(self):
        return f"{self.customer.username} - {self.package.name}"


class WorkoutLog(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trainer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="trainer_logs",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    workout_types = models.ManyToManyField(WorkoutType)
    date = models.DateField()
    duration = models.DurationField()
    notes = models.TextField(blank=True)
    user_package = models.ForeignKey(
        UserPackage, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        workout_types = ", ".join([wt.name for wt in self.workout_types.all()])
        return f"{self.customer.username} - {workout_types} on {self.date}"
