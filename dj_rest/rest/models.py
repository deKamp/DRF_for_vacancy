from django.db import models
import uuid

class WeekDay(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)

class Availability(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.pk)

# ***************************************************

class Teacher(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    image = models.FileField(upload_to='teachers/')

    def __str__(self):
        return self.short_name

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=50)
    startTime = models.TimeField(auto_now=False)
    endTime = models.TimeField(auto_now=False)
    weekDay = models.ForeignKey(WeekDay, on_delete=models.SET_NULL, null=True)
    appointment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    service_id = models.UUIDField(default=uuid.uuid4, editable=False)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    color = models.CharField(max_length=7)
    availability = models.ForeignKey(Availability, on_delete=models.SET_NULL, null=True)
    teacher_v2 = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
