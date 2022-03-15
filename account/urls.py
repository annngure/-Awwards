from django.urls import path,re_path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index, name= "index"),
    path('profile/',views.profileView, name="profile"),
    path('login/',LoginView.as_view(), name="login"),
    path('register/',views.registerView,name="register"),
    path('logout/',LogoutView.as_view(next_page ="index"), name="logout"),
    path('upload/profile',views.update_profile,name ="upadate-profile"),
    path('comment/',views.comment, name ='comment')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    



