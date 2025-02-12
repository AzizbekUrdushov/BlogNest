from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout as auth_logout
from .models import TextBlog, PhotoBlog, VideoBlog, AudioBlog, CustomUser, Reaction
from .forms import NewTextBlog, NewAudioBlog, NewPhotoBlog, NewVideoBlog, BloggerUserSignUpForm, RegularUserSignUpForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.contenttypes.models import ContentType


# Create your views here.
@login_required
def home(response):
    user = response.user  # Get the currently logged-in user
    context = {
        'profile_picture': user.profile_picture.url if user.profile_picture else 'circle-user-solid.svg',
        'username': user.username,
        'name': user.name,
        'surname': user.surname,
        'bio': user.bio if hasattr(user, 'bio') else ''
    }
    return render(response, 'basic/base.html', context)


def text(response):
    text = TextBlog.objects.select_related('user').all().order_by('-uploaded_at')  
    
    return render(response, 'basic/text_post.html', {'t':text,})
@csrf_exempt  # Temporarily disable CSRF protection for testing
def callajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging line

            # Reaction handling
            if 'blog_id' in data and 'reaction' in data:
                blog_id = data.get('blog_id')
                reaction = data.get('reaction')
                print("Reaction request:", blog_id, reaction)  # Debugging line

                blog = TextBlog.objects.get(pk=blog_id)
                if reaction == 'like':
                    blog.like_count += 1
                elif reaction == 'dislike':
                    blog.dislike_count += 1
                elif reaction == 'love':
                    blog.love_count += 1
                elif reaction == 'fire':
                    blog.fire_count += 1
                elif reaction == 'sad':
                    blog.sad_count += 1
                
                blog.save()
                return JsonResponse({
                    "success": True,
                    "message": f"You reacted with {reaction} successfully!"
                })

            # Loading posts
            counter = int(data.get('counter', 0))
            obj = TextBlog.objects.select_related('user').order_by('-uploaded_at')[counter:counter + 5]

            serialized_data = serializers.serialize('json', obj)



            return JsonResponse({"data": serialized_data}, safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)




def photo(response):
    photos = PhotoBlog.objects.all().order_by('-uploaded_at')

    return render(response, 'basic/photo_posts.html', {'p':photos,})

def call_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging line

            # Reaction handling
            if 'blog_id' in data and 'reaction' in data:
                blog_id = data.get('blog_id')
                reaction = data.get('reaction')
                print("Reaction request:", blog_id, reaction)  # Debugging line

                blog = PhotoBlog.objects.get(pk=blog_id)
                if reaction == 'like':
                    blog.like_count += 1
                elif reaction == 'dislike':
                    blog.dislike_count += 1
                elif reaction == 'love':
                    blog.love_count += 1
                elif reaction == 'fire':
                    blog.fire_count += 1
                elif reaction == 'sad':
                    blog.sad_count += 1
                
                blog.save()
                return JsonResponse({
                    "success": True,
                    "message": f"You reacted with {reaction} successfully!"
                })

            # Loading posts
            counter = int(data.get('counter', 0))
            obj = PhotoBlog.objects.all().order_by('-uploaded_at')[counter:counter + 5]
            serialized_data = serializers.serialize('json', obj)
            return JsonResponse({"data": serialized_data}, safe=False)

        except Exception as e:
            print("Error:", str(e))  # Debugging line
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


def video(response):
    video = VideoBlog.objects.all().order_by('-uploaded_at')


    return render(response, 'basic/video_post.html', {'v':video,})

def callajax1(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging line

            # Reaction handling
            if 'blog_id' in data and 'reaction' in data:
                blog_id = data.get('blog_id')
                reaction = data.get('reaction')
                print("Reaction request:", blog_id, reaction)  # Debugging line

                blog = VideoBlog.objects.get(pk=blog_id)
                if reaction == 'like':
                    blog.like_count += 1
                elif reaction == 'dislike':
                    blog.dislike_count += 1
                elif reaction == 'love':
                    blog.love_count += 1
                elif reaction == 'fire':
                    blog.fire_count += 1
                elif reaction == 'sad':
                    blog.sad_count += 1
                
                blog.save()
                return JsonResponse({
                    "success": True,
                    "message": f"You reacted with {reaction} successfully!"
                })

            # Loading posts
            counter = int(data.get('counter', 0))
            obj = VideoBlog.objects.all().order_by('-uploaded_at')[counter:counter + 5]
            serialized_data = serializers.serialize('json', obj)
            return JsonResponse({"data": serialized_data}, safe=False)

        except Exception as e:
            print("Error:", str(e))  # Debugging line
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


def audio(response):
    audio = AudioBlog.objects.all().order_by('-uploaded_at')


    return render(response, 'basic/audio_post.html', {'a':audio,})

@csrf_exempt  # Temporarily disable CSRF protection for testing
def callajax2(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Reaction handling
            if 'blog_id' in data and 'reaction' in data:
                blog_id = data.get('blog_id')
                reaction = data.get('reaction')
                print("Reaction request for AudioBlog:", blog_id, reaction)  # Debugging line

                blog = AudioBlog.objects.get(pk=blog_id)
                if reaction == 'like':
                    blog.like_count += 1
                elif reaction == 'dislike':
                    blog.dislike_count += 1
                elif reaction == 'love':
                    blog.love_count += 1
                elif reaction == 'fire':
                    blog.fire_count += 1
                elif reaction == 'sad':
                    blog.sad_count += 1
                
                blog.save()
                return JsonResponse({"success": True, "message": f"You reacted with {reaction} successfully!"})

            # Loading more audio posts
            counter = int(data.get('counter', 0))
            obj = AudioBlog.objects.all().order_by('-uploaded_at')[counter:counter + 5]
            serialized_data = serializers.serialize('json', obj)
            
            return JsonResponse({"data": serialized_data}, safe=False)
        
        except Exception as e:
            print("Error:", str(e))  # Debugging line
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Invalid request"}, status=400)





# FORMS 
def create_text(response):
    if response.method == 'POST':
        form = NewTextBlog(response.POST)

        if form.is_valid():
            user=response.user,
            title = form.cleaned_data['title']
            content = form.cleaned_data['text']
            t_blog = TextBlog(title=title, text=content)
            t_blog.save()

            messages.success(response, "Uploaded successfully!")

            return redirect('/')

            #reset
            form = NewTextBlog()




    else:
        form = NewTextBlog()

     
    return render(response, 'forms/create_text.html', {'form':form})


def create_photo(response):
    if response.method == 'POST':
        form = NewPhotoBlog(response.POST, response.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            photo = form.cleaned_data['photo']
            content = form.cleaned_data['description']
            p_blog = PhotoBlog(title=title, image = photo , description=content)
            p_blog.save()

            messages.success(response, "Uploaded successfully!")

            return redirect('/')

            #reset
            form = NewPhotoBlog()


    else:
        form = NewPhotoBlog()
     
    return render(response, 'forms/create_photo.html', {'form':form})


def create_audio(response):
    if response.method == 'POST':
        form = NewAudioBlog(response.POST, response.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            audio = form.cleaned_data['audio']
            content = form.cleaned_data['description']
            a_blog = AudioBlog(title=title, audio = audio , description=content)
            a_blog.save()


            messages.success(response, "Uploaded successfully!")

            return redirect('/')

            #reset
            form = NewAudioBlog()

    else:
        form = NewAudioBlog()
     
    return render(response, 'forms/create_audio.html', {'form':form})


def create_video(response):
    if response.method == 'POST':
        form = NewVideoBlog(response.POST, response.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            video = form.cleaned_data['video']
            content = form.cleaned_data['description']
            v_blog = VideoBlog(title=title, video = video , description=content)
            v_blog.save()

            messages.success(response, "Uploaded successfully!")

            return redirect('/')

            #reset
            form = NewVideoBlog()

    else:
        form = NewVideoBlog()
     
    return render(response, 'forms/create_video.html', {'form':form})





@csrf_exempt
def add_reaction(request):
    if request.method == "POST":
        data = json.loads(request.body)
        blog_id = data.get('blog_id')
        reaction = data.get('reaction')
        
        try:
            blog = TextBlog.objects.get(id=blog_id)
            if reaction == 'like':
                blog.like_count += 1
            elif reaction == 'dislike':
                blog.dislike_count += 1
            # Add other reactions like love, fire, sad, etc.
            blog.save()
            return JsonResponse({"success": True, "reaction_count": blog.like_count})  # Return updated count
        except TextBlog.DoesNotExist:
            return JsonResponse({"success": False, "error": "Blog not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})


    

#signup and login forms

def blogger_user_signup(request):
    if request.method == 'POST':
        form = BloggerUserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.name = form.cleaned_data.get('name')
            user.surname = form.cleaned_data.get('surname')
            login(request, user)
            return HttpResponseRedirect(reverse('login'))

    else:
        form = BloggerUserSignUpForm()
    return render(request, 'registration/signup.html', {'form':form, 'user_type': 'Blogger'})

def regular_user_signup(request):
    if request.method == 'POST':
        form = form = RegularUserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.name = form.cleaned_data.get('name')
            user.surname = form.cleaned_data.get('surname')
            login(request, user)
            return HttpResponseRedirect(reverse('login'))

    else:
        form = RegularUserSignUpForm()
    return render(request, 'registration/signup.html', {'form':form, 'user_type': 'Regular'})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  # Save changes
            return redirect('home')  # Redirect after saving
        else:
            print(form.errors)  # Debugging: Print form errors
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'forms/edit_profile.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm

    def form_invalid(self, form):
        """This will be called when the form is invalid."""
        return self.render_to_response(self.get_context_data(form=form))

def custom_logout(request):
    if request.method == "POST":
        auth_logout(request)  # This calls Django's built-in logout function
        return redirect('/')  # Redirect to home page after logging out
    return render(request, 'registration/logout.html')







def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def custom_400(request, exception):
    return render(request, 'errors/400.html', status=400)