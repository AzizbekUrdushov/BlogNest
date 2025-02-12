from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import handler404, handler500, handler403, handler400
from . import views 
from .views import callajax, call_ajax, callajax1, callajax2, blogger_user_signup, regular_user_signup, CustomLoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.home, name="home"),

    path('edit-profile/', views.edit_profile, name='edit_profile'),

     path('add_reaction/', views.add_reaction, name='add_reaction'),

     path('favicon.ico', lambda request: HttpResponse(status=204)),  # Return empty response


    path("text_post", views.text, name="text"),
    path("photo_post", views.photo, name="photo"),
    path("video_post", views.video, name="video"),
    path("audio_post", views.audio, name="audio"),

    path("create_text_post", views.create_text, name="create_text"),
    path("create_photo_post", views.create_photo, name="create_photo"),
    path("create_audio_post", views.create_audio, name="create_audio"),
    path("create_video_post", views.create_video, name="create_video"),

    path('callajax/', callajax, name='callajax'),
    path('call_ajax/', call_ajax, name='call_ajax'),
    path('callajax1/', callajax1, name='callajax1'),
    path('callajax2/', callajax2, name='callajax2'),

    path('signup/blogger/', blogger_user_signup, name='blogger_signup'),
    path('signup/user/', regular_user_signup, name='regular_user_signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)