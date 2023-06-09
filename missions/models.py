from django.db import models
from django.contrib.auth.models import User

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

STATUS = (
    (1, 'Active'),
    (2, 'Completed'),
    (3, 'On Hold'),
    (4, 'Cancelled')
)

PUBLISH = ((0, 'Hidden'), (1, 'Displayed'))


class Mission(models.Model):
    """Set up our model for missions"""
    mission = models.CharField(
        max_length=100, null=False, blank=False, unique=True)
    mission_grade = models.IntegerField(choices=GRADES, default=5)
    mission_lead = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name="missions")
    description = models.TextField(max_length=2000, null=False, blank=False)
    prep_time = models.PositiveIntegerField(default=5)  # number in days
    mission_length = models.PositiveIntegerField(default=1)  # number in weeks
    mission_status = models.IntegerField(choices=STATUS, default=1)
    mission_img = models.ImageField(null=True, blank=True)
    img_url = models.URLField(max_length=1024, null=True, blank=True)
    approved_mission = models.IntegerField(choices=PUBLISH, default=0)

    class Meta:
        """Set up our extra model settings"""
        ordering = [
            'mission'
        ]

    def __str__(self):
        return self.mission

class Update(models.Model):
    """set up our new model for updates"""
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=100, default='')
    body = models.TextField(default='', max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.PositiveIntegerField(choices=PUBLISH, default=0)

    class Meta:
        """set up class meta for Updates"""
        ordering = [
            'mission',
            'created_on'
        ]

    def __str__(self):
        return self.title
