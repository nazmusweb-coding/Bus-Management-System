from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.about_us, name="about_us"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('blog', views.blog_list, name='blog'),
    path('gallery', views.gallery_list, name='gallery_list'),
    path('gallery/<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('cookies', views.cookies_view, name='cookies'),
    path('legal-notice', views.legal_notice_view, name='legal_notice'),
    path('privacy-policy', views.privacy_policy_view, name='privacy_policy'),
    path('terms', views.terms, name='terms'),
    path('refund', views.refund, name='refund'),
    path('verify-invoice', views.invoice_verify_view, name='verify_invoice'),
    path('check/bookings', views.admin_booking_view, name='admin_booking_view'),
    path('check/buses/', views.admin_bus_list, name='admin_bus_list'),
    path('check/buses/add/', views.add_bus, name='add_bus'),
    path('check/buses/edit/<int:bus_id>/', views.edit_bus, name='edit_bus'),
    path('check/buses/delete/<int:bus_id>/', views.delete_bus, name='delete_bus'),
    path('manage/bookings/', views.admin_manage_bookings, name='admin_manage_bookings'),
    path('manage/bookings/create/', views.create_booking, name='create_booking'),
    path('manage/bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('manage/bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('manage/bookings/rebook/<int:booking_id>/', views.rebook_booking, name='rebook_booking'),
    path('manage/gallery/', views.manage_gallery, name='manage_gallery'),
    path('manage/gallery/new/', views.create_or_edit_gallery, name='create_or_edit_gallery'),
    path('manage/gallery/edit/<int:pk>/', views.create_or_edit_gallery, name='create_or_edit_gallery'),
    path('manage/gallery/delete/<int:pk>/', views.delete_gallery, name='delete_gallery'),
    path('manage-blogs', views.manage_blogs, name='manage_blogs'),
    path('blog/new', views.edit_blog, name='new_blog'),
    path('blog/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('blog/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('bus/<int:bus_id>/', views.bus_detail, name='bus_detail'), # View bus review details
    # path('bus/<int:bus_id>/review/', views.add_review, name='add_review'),
    path('review/<int:bus_id>/', views.add_review, name='add_review'),
    path('invoice/<int:booking_id>/', views.download_invoice, name='download_invoice'),
    path('suggestions/', views.get_suggestions, name='suggestions'),
    path('api/booked-seats/', views.get_booked_seats, name='get_booked_seats'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)