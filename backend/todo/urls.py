from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

def root_view(request):
  return HttpResponse('Welcome, Everything is Fine!')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', root_view),
  path('/api', include(router.urls)),
]
