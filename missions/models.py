from django.db import models

from personnel.models import Personnel

# Create your models here.
GRADES = (
    (1, 'Extreme'),
    (2, 'Dangerous'),
    (3, 'Serious'),
    (4, 'Moderate'),
    (5, 'Basic'),
    (6, 'Training')
)
class Mission(models.Model):
    """Set up our model for missions"""
    mission = models.CharField(max_length=100, null=False, blank=False, unique=True)
    mission_grade = models.IntegerField(choices=GRADES, default=5)
    mission_lead = models.ForeignKey(Personnel, on_delete=models.Cascade)
    description = models.TextField(max_length=2000, null=False, blank=False)
    prep_time = models.PositiveIntegerField(max_length=2, default=5) #number in days
    mission_length = models.PositiveIntegerField(max_length=1, default=1) #number in weeks

    class Meta:
        """Set up our extra model settings"""
        ordering = ['grade']

    def __str__(self):
        return self.mission
