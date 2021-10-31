#from django.contrib import admin
from django.urls import path, include
from . import views
# routers allow to create get and post requests (from website itself)
from rest_framework import routers 

router = routers.DefaultRouter()
# audios is the url I want to show
router.register('audios', views.AudioView)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
]