from django.db import models

class MotionAlert(models.Model):
    home_id = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Unresolved')
    image = models.ImageField(upload_to='alerts/', blank=True, null=True)

    def __str__(self):
        return f"{self.home_id} - {self.status}"
