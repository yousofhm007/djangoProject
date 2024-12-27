
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learning_logs/', include('learning_logs.urls')),
]
