from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]}. {self.middle_name[:1]}. ({self.pk})'


class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Teacher(Person):
    subjects = models.ManyToManyField(Subject, blank=True)

    class Meta:
        ordering = ('id',)
        permissions = (
            ('access_lk', 'Доступ в ЛК'),
        )


class Student(Person):
    subjects = models.ManyToManyField(Subject, blank=True)

    class Meta:
        ordering = ('id',)
