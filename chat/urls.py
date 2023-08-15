from django.urls import path, include
from chat.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', chatpage, name="chatpage"),

	# login-section
	path('signin/', signin, name='signin'),
	path('signout/', signout, name='signout'),
	path('signup/', signup, name='signup'),

	]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

