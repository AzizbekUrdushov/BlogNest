from django.db import models
from django.utils import timezone, timesince
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Custom User model
class CustomUser(AbstractUser):
    is_blogger = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.name} {self.surname})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




# Blog models
class TextBlog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    love_count = models.IntegerField(default=0)
    fire_count = models.IntegerField(default=0)
    sad_count = models.IntegerField(default=0)



    def __str__(self):
        return self.title

class PhotoBlog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=150)
    u_name = CustomUser.username
    profile_image = CustomUser.profile_picture
    uploaded_at = models.DateTimeField(default=timezone.now)

    def time_ago(self):
        now = timezone.now()
        return timesince(self.uploaded_at, now)

    def __str__(self):
        return f'{self.title} \n{self.image} \n{self.description}'


class VideoBlog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to='videos/')
    description = models.CharField(max_length=150)
    u_name = CustomUser.username
    profile_image = CustomUser.profile_picture
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} \n{self.video} \n{self.description}'


class AudioBlog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    audio = models.FileField(upload_to='audio/')
    description = models.TextField()
    u_name = CustomUser.username
    profile_image = CustomUser.profile_picture
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} \n{self.audio} \n{self.description}'


# Reaction model
class Reaction(models.Model):
    REACTION_TYPES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('love', 'Love'),
        ('fire', 'Fire'),
        ('sad', 'Sad'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Generic relation to any blog type
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    reaction = models.CharField(max_length=10, choices=REACTION_TYPES)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')  # Ensures one reaction per user per blog

    def __str__(self):
        return f"{self.user.username} reacted {self.reaction} on {self.content_object}"
