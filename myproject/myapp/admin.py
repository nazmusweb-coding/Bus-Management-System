from django.contrib import admin
from .models import Bus, User, Book, Blog, TravelGallery, Review, Seat

# Register your models here.

admin.site.register(Bus)
# admin.site.register(User)
admin.site.register(Book)
admin.site.register(Blog)
admin.site.register(TravelGallery)
admin.site.register(Review)
admin.site.register(Seat)
