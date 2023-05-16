from django.urls import path
from django.contrib import admin
import my_pet.views

from django.conf.urls.static import static
from django.conf import settings

app_name='my_pet'

urlpatterns = [
    path('', my_pet.views.index, name='index'),
    path('admin/', admin.site.urls),
    # URL:8000/my_pet에 접속하면 my_pet 페이지 + URL이름은 my_pet이다
    path('my_pet/', my_pet.views.my_pet, name='my_pet'),
    # URL:8000/my_pet/숫자로 접속하면 게시글-세부페이지(posting)
    path('my_pet/<int:post_id>', my_pet.views.posting, name='posting'),
    path('my_pet/new_post/', my_pet.views.new_post),
    path('my_pet/<int:post_id>/remove_post', my_pet.views.delete_post),
    path('my_pet/<int:post_id>/update_post', my_pet.views.update_post),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)