from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect  # Add this import
from users import views as user_views
from books import views as book_views
from orders import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('signup/', user_views.signup_view, name='signup'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    
    # Book URLs
    path('books/', book_views.book_list, name='book_list'),
    path('books/<int:book_id>/', book_views.book_detail, name='book_detail'),
    
    # Order URLs
    path('add-to-cart/<int:book_id>/', order_views.add_to_cart, name='add_to_cart'),
    path('cart/', order_views.cart, name='cart'),
    path('confirm-order/', order_views.confirm_order, name='confirm_order'),
    path('payment/', order_views.payment, name='payment'),
    
    # Redirect root to book list
    path('', lambda request: redirect('book_list')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
