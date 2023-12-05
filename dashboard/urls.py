from django.urls import path
from dashboard.views import dashboard, website_view, website_delete, website_edit, website_create

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='home'),
    path('website/create/', website_create, name='website-create'),
    path('website/<int:pk>/', website_view, name='website-details'),
    path('website/<int:pk>/delete/', website_delete, name='website-delete'),
    path('website/<int:pk>/edit/', website_edit, name='website-edit')
]
