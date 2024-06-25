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
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
 
    ##### user related path########################## 
    path('', include('blog.urls')),
    path('login/', blog_view.login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/', blog_view.register, name ='register'),
    path('safe/',blog_view.safe,name='safe'),
    path('tkt/',blog_view.tkt,name='tkt'),
    path('postindex/',blog_view.post_index,name='postindex'),
    path('post/<int:pk>/', blog_view.blog_detail, name='blog_detail'),
    path('category/<str:category_name>/', blog_view.blog_category, name='blog_category'),
  
    
    
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)