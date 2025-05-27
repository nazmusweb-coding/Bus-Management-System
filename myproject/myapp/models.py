# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

# Create your models here.

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     email = models.EmailField()
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)

#     def __str__(self):
#         return self.email


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=4)  # e.g., A1, B2
    date = models.DateField()
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    booking = models.ForeignKey('Book', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('bus', 'seat_number', 'date')

    def __str__(self):
        return f"{self.bus.bus_name} - Seat {self.seat_number} ({self.date})"


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = (
        (BOOKED, 'BOOKED'),
        (CANCELLED, 'CANCELLED'),
    )

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid = models.IntegerField()  # Could also be ForeignKey(User, on_delete=...)
    busid = models.IntegerField()   # Could also be ForeignKey(Bus, on_delete=...)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    date = models.DateField()
    time = models.TimeField()
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return f"Booking: {self.name} ({self.email}) - {self.bus_name} on {self.date}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)  # Assuming you have a Bus model
    rating = models.PositiveSmallIntegerField(default=5)   # 1 to 5 stars
    comment = models.TextField(max_length=200)
    
    # Additional fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)  # optional
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} for {self.bus.bus_name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class TravelGallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='gallery_photos/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'phone', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'phone': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }

class TravelGalleryForm(forms.ModelForm):
    class Meta:
        model = TravelGallery
        fields = ['title', 'description', 'photo']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'oninput': 'updatePreview()'}),
            'title': forms.TextInput(attrs={'oninput': 'updatePreview()'})
        }

class BusForm(forms.ModelForm):
    source = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'id': 'source',
            'list': 'suggested-sources',
            'placeholder': 'Source',
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )
    dest = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'id': 'destination',
            'list': 'suggested-destinations',
            'placeholder': 'Destination',
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    time = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'id': 'time',  # Fixed duplicated id="destination" — changed to "time"
            'list': 'suggested-times',
            'placeholder': 'HH:MM AM/PM',
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = Bus
        fields = ['bus_name', 'source', 'dest', 'nos', 'rem', 'price', 'date', 'time']

    def clean_time(self):
        time_str = self.cleaned_data['time']
        try:
            # Convert from 12-hour string (e.g., "02:30 PM") to Python time object
            time_obj = datetime.strptime(time_str.strip(), "%I:%M %p").time()
            return time_obj
        except ValueError:
            raise forms.ValidationError("Enter a valid time in 12-hour format (e.g., 02:30 PM)")
