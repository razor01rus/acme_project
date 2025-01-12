# Импортируем настройки проекта.
from django.conf import settings # type: ignore
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.views.generic.edit import CreateView # type: ignore
from django.contrib import admin # type: ignore
from django.urls import include, path, reverse_lazy # type: ignore

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

handler404 = 'core.views.page_not_found' 

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

# Подключаем функцию static() к urlpatterns:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


