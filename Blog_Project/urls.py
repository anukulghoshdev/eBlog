
from django.contrib import admin
from django.urls import path, include

from . import views


from django.conf import settings # for imgae/media
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('account/', include('App_RegLog.urls')),
    path('blog/', include('App_Blog.urls')),
    # path('myapp1/', include('myapp1.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
