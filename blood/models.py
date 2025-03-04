# models.py

from django.db import models

# User Model (Base Model for Donor, Recipient, Organization roles)
class User(models.Model):
    ROLE_CHOICES = [
        ('Donor', 'Donor'),
        ('Recipient', 'Recipient'),
        ('Organization', 'Organization'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)  # Ideally hashed
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Donor Model
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_profile')
    blood_group = models.CharField(max_length=10)
    age = models.IntegerField()
    medical_history = models.TextField()
    eligibility_status = models.BooleanField(default=True)
    last_donation_date = models.DateField()
    reminder_preferences = models.TextField()  # Format: JSON or plain text

    def __str__(self):
        return self.user.name


# Recipient Model
class Recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipient_profile')
    blood_group = models.CharField(max_length=10)
    medical_history = models.TextField()
    emergency_request = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    request_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Fulfilled', 'Fulfilled'), ('Urgent', 'Urgent')])

    def __str__(self):
        return self.user.name


# Organization Model (Hospital/Organization)
class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization_profile')
    name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    location = models.CharField(max_length=255)
    blood_inventory = models.JSONField()  # Stores blood types and quantities

    def __str__(self):
        return self.name


# BloodRequest Model
class BloodRequest(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, related_name='blood_requests')
    hospital = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='blood_requests')
    blood_type_required = models.CharField(max_length=10)
    quantity_needed = models.IntegerField()
    urgency_level = models.CharField(max_length=20, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Fulfilled', 'Fulfilled'), ('Cancelled', 'Cancelled')])
    request_date = models.DateField()

    def __str__(self):
        return f'{self.blood_type_required} request by {self.recipient.user.name}'


# BloodDonation Model
class BloodDonation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donations')
    blood_type_donated = models.CharField(max_length=10)
    donation_date = models.DateField()
    quantity_donated = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')])
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.donor.user.name} donated {self.blood_type_donated}'


# BloodBank Model
class BloodBank(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    available_blood_types = models.JSONField()  # Blood types and their available quantities

    def __str__(self):
        return self.name


# DonationCamp Model
class DonationCamp(models.Model):
    hospital = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='donation_camps')
    location = models.CharField(max_length=255)
    scheduled_date = models.DateField()
    blood_types_targeted = models.JSONField()  # List of blood types needed at this camp

    def __str__(self):
        return f'Donation camp at {self.location} on {self.scheduled_date}'
