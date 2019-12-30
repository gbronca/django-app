from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Ticket(models.Model):
    STATUS = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    )

    ISSUE = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature')
    )

    title = models.CharField(max_length=75)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS,default='Pending')
    issue = models.CharField(max_length=20, choices=ISSUE, default='Bug')
    upvotes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('tickets:detail', kwargs={'pk': self.pk})



class Comments(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    comment = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ticket}: {self.username}'

    def get_absolute_url(self):
        return reverse("ticket:detail")


class Upvoted(models.Model):
    ticket = models.ForeignKey(Ticket, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.ticket}'