from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('temp', views.temp, name='temp'),
    path('test', views.test, name='test'),
    path('rating', views.rating, name='rating'),
    path('post_rating', views.post_rating, name='post_rating'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
