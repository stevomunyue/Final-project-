from django.db import models

from django.db import models

class Appointment(models.Model):
    SESSION_TYPES = [
        ('In-Person', 'In-Person'),
        ('Virtual', 'Virtual'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateField()
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES)
    additional_notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.session_type}"
from django.db import models

class Appointment(models.Model):
    # Appointment details
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateField()
    session_type = models.CharField(max_length=20, choices=(('in-person', 'In-Person'), ('virtual', 'Virtual')))
    additional_notes = models.TextField(blank=True, null=True)
    
    # Payment details
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    
    # Image upload
    uploaded_image = models.ImageField(upload_to='appointments/', blank=True, null=True)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date}"

