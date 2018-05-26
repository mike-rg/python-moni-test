from django.db import models

from django.utils.translation import ugettext_lazy as _


class Loan(models.Model):
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    )
    dni = models.CharField(max_length=8)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(help_text=_('Example: fran@mail.com'))
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.dni