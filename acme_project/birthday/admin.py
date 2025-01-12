from django.contrib import admin # type: ignore

# Из модуля models импортируем модель...
from .models import Birthday, Tag

# ...и регистрируем её в админке:
admin.site.register(Birthday)
admin.site.register(Tag) 