from django.contrib import admin
from .models import Project

# Регистрируем модель Project в админке
admin.site.urls
admin.site.register(Project)