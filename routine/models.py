from django.contrib.auth.models import User
from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class Title(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class CourseDuration(models.Model):
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.duration


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_number = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Program(models.Model):
    program_name = models.CharField(max_length=255)
    duration = models.ForeignKey(CourseDuration, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='+')

    def __str__(self):
        return self.program_name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField()
    nrc_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=14)
    email_address = models.EmailField(max_length=64)
    guardian_phone_number = models.CharField(max_length=14, blank=True, null=True)
    residential_address = models.CharField(max_length=255, blank=True, null=True)
    program_enrolled = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    date_enrolled = models.DateField(blank=True, null=True)
    graduating_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name


class LecturerProfile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    birth_date = models.DateField()
    nrc_number = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=14)
    email_address = models.EmailField(max_length=64)
    courses_teaching = models.ManyToManyField(Course, related_name='+')


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploads = models.FileField()
    published_date = models.DateField(auto_now=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructions = models.TextField()

    def __str__(self):
        return self.title


class Announcement(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Resource(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    upload = models.FileField()

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    logo = models.ImageField()
    motto = models.CharField(max_length=255)
    name_of_principal = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    number_of_programs = models.IntegerField()

    def __str__(self):
        return self.name


class AssignmentResponse(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

