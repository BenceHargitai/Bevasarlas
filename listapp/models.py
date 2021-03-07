from django.db import models

# Create your models here.

class Lista(models.Model):
    """Model definition for Lista."""
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=10)
    nameid = models.CharField(max_length=40)

    class Meta:
        """Meta definition for Listák."""

        verbose_name = 'Lista'
        verbose_name_plural = 'Lista'

    def __str__(self):
        return f"{self.name} - {self.amount} - (id : {self.nameid})"
