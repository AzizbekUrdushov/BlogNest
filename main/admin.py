from django.contrib import admin
from .models import TextBlog, PhotoBlog, VideoBlog, AudioBlog, CustomUser
# Register your models here.


admin.site.register(TextBlog)
admin.site.register(PhotoBlog)
admin.site.register(VideoBlog)
admin.site.register(AudioBlog)
admin.site.register(CustomUser)
