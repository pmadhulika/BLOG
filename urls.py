"""from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('blog.urls'))

]"""
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_view
from django.contrib.auth import views as auth
from django.contrib.auth import login as auth_login
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
 
    ##### user related path########################## 
    path('', include('blog.urls')),
    path('login/', blog_view.login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/', blog_view.register, name ='register'),
    path('safe/',blog_view.safe,name='safe'),
    path('tkt/',blog_view.tkt,name='tkt')
]