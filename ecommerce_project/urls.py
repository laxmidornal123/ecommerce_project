from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views   # 🔥 ADD THIS

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='/'),
        name='logout'
    ),

    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)