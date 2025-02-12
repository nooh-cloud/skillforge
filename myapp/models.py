from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # Duration in hours
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    level = models.CharField(
        max_length=50,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')]
    )
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    content = models.TextField()
    video = models.FileField(upload_to='lessons/videos/', blank=True, null=True)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trainer_profile')
    expertise = models.CharField(max_length=300)
    bio = models.TextField(max_length=400)
    profile_picture = models.ImageField(upload_to='trainer_profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='student_profiles/', blank=True, null=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='students', blank=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"

class Certification(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='certifications')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certifications')
    issue_date = models.DateTimeField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    
    def __str__(self):
        return f"Certificate for {self.course.title} - {self.student.user.username}"

class Review(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 rating
    feedback = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.student.user.username} - {self.course.title}"

class Transaction(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='transactions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction by {self.student.user.username} for {self.course.title}"
