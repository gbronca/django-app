from django.db import models
# from django.contrib.auth.models import User
# from tickets.models import Ticket

# class Cart(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     ticket = models.ManyToManyField(Ticket, blank=True)
#     total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
#     updated = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.id)