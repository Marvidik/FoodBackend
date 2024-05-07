"""
URL configuration for FoodBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from authentication import views
from savvyfoods import views as foodviews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Urls for all authentications and user profile infos
    path('admin/', admin.site.urls),
    path('login/',views.login, name="login"),
    path('signup/',views.register,name="register"),
    path('password/reset/', views.password_reset, name='password_reset'),
    path('password/reset/confirm', views.password_reset_confirm, name='password_reset_confirm'),
    path("otp/",views.confirm_otp,name="confirm_otp"),

    path('restaurants/',foodviews.restaurants,name="restaurant"),
    path('restaurant/food/<id>',foodviews.restaurant_food,name="restaurant-food"),
    path('restaurant/junk/<id>',foodviews.restaurant_junk,name="restaurant-junk"),


    path('cart/<id>',foodviews.view_cart,name="view-cart"),
    path('addcart/',foodviews.add_to_cart,name="add-to-cart"),
    path('removecart/<id>',foodviews.remove_from_cart,name="remove-from-cart"),


    path('delivered/<pk>',foodviews.received,name="received"),
    path("addorder/",foodviews.add_to_order,name="add-order"),
    path("vieworder/<id>",foodviews.view_orders,name="view-orders"),


    path('ads/',foodviews.advert,name="advert"),

    path("profile/<id>",views.profile_get,name="profile"),
    path("profile/add/",views.profile_add,name="add-profile"),
    path('profiles/<int:profile_id>/', views.profile_delete, name='profile_delete'),
]


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns+= staticfiles_urlpatterns()