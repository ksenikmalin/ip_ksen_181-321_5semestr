from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.ServicesView.as_view()),
    path("services/", views.ServicesListAPIView.as_view()),
    path("<int:pk>/", views.ServicesDetailView.as_view()),
    path("recipe/<int:pk>", views.ServicesDetailAPIView.as_view()),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    