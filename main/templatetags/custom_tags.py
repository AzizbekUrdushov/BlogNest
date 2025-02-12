from django import template

register = template.Library()

@register.filter
def not_in_create_pages(path):
    create_pages = ['/create_audio_post/', '/create_video_post/', '/create_photo_post/', '/create_text_post/']
    return path not in create_pages
