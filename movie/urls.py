from django.urls import path,include
from . import views
from user_profile import views as uviews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('search/',views.search,name="search"),
    path('',views.home,name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/",uviews.out,name="out"),
    path('register/', uviews.register, name='register'),
    path('profile/', uviews.profile, name='profile'),
    path('news/',views.news,name='news')
    
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)