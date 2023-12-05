from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('users/', include('users.urls', namespace='users')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('language/', set_language, name='set_language'),

    path('', include('app.urls', namespace='app'))

]
