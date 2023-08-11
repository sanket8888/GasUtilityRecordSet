from django.db import models

class ServiceRequest(models.Model):
    TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Gas Odor', 'Gas Odor'),
        ('Meter Reading', 'Meter Reading'),
        # Add more types as needed
    )

    customer_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50, choices=TYPES)
    request_details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.request_type}"
