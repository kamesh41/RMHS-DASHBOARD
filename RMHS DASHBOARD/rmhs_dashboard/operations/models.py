from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Choices for shift
SHIFT_CHOICES = [
    ('A', 'Shift A (6:00 AM - 2:00 PM)'),
    ('B', 'Shift B (2:00 PM - 10:00 PM)'),
    ('C', 'Shift C (10:00 PM - 6:00 AM)'),
    ('G', 'General Shift (9:00 AM - 6:30 PM)'),
]

# Choices for material types
MATERIAL_CHOICES = [
    ('IRON_ORE', 'Iron Ore'),
    ('LIMESTONE', 'Limestone'),
    ('DOLOMITE', 'Dolomite'),
    ('COAL', 'Coal'),
    ('COKE', 'Coke'),
    ('SINTER', 'Sinter'),
    ('PELLET', 'Pellet'),
    ('OTHER', 'Other'),
]

class Area1Operation(models.Model):
    """Model for Area-1 operations (Reclaiming, Feeding to BF/SMS, Receiving from BF)"""
    date = models.DateField(default=timezone.now)
    shift = models.CharField(max_length=1, choices=SHIFT_CHOICES)
    
    # Reclaiming
    reclaiming_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    reclaiming_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    reclaiming_equipment = models.CharField(max_length=50, help_text="Equipment used for reclaiming")
    
    # Feeding
    feeding_destination = models.CharField(max_length=50, help_text="Destination (BF/SMS)")
    feeding_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    feeding_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    feeding_equipment = models.CharField(max_length=50, help_text="Equipment used for feeding")
    
    # Receiving
    receiving_source = models.CharField(max_length=50, help_text="Source (BF)")
    receiving_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    receiving_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    receiving_equipment = models.CharField(max_length=50, help_text="Equipment used for receiving")
    
    # Common fields
    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='area1_operations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Area-1 Operation"
        verbose_name_plural = "Area-1 Operations"
    
    def __str__(self):
        return f"Area-1 Operation - {self.date} - Shift {self.shift}"


class Area23Operation(models.Model):
    """Model for Area-2 & Area-3 operations (Feeding, Receiving, Crushing, Base Mix Handling)"""
    date = models.DateField(default=timezone.now)
    shift = models.CharField(max_length=1, choices=SHIFT_CHOICES)
    
    # Feeding
    feeding_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    feeding_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    feeding_equipment = models.CharField(max_length=50, help_text="Equipment used for feeding")
    
    # Receiving
    receiving_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    receiving_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    receiving_equipment = models.CharField(max_length=50, help_text="Equipment used for receiving")
    
    # Crushing
    crushing_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    crushing_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    crushing_equipment = models.CharField(max_length=50, help_text="Equipment used for crushing")
    
    # Base Mix Handling
    base_mix_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    base_mix_quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in MT")
    base_mix_equipment = models.CharField(max_length=50, help_text="Equipment used for base mix handling")
    
    # Common fields
    remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='area23_operations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Area-2 & 3 Operation"
        verbose_name_plural = "Area-2 & 3 Operations"
    
    def __str__(self):
        return f"Area-2 & 3 Operation - {self.date} - Shift {self.shift}" 