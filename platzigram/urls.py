from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views



urlpatterns = [
    path('', local_views.home),
    path('admin/', admin.site.urls),
    path('saludo/<str:name>/<int:age>/', local_views.saludo, name='hi'),
    path('saludoquery/', local_views.saludoQuery),
    path('posts/',posts_views.list_posts, name='feed'),
    path('users/login', users_views.login_view, name='login'),
    path('users/logout', users_views.logout_view, name='logout'),
    path('users/signup', users_views.signup_view, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ## Este codigo sumado permite ver las imagenes desde el navegador
