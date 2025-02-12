from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

#forms for create Posts
class NewTextBlog(forms.Form):
    title = forms.CharField(label='Enter your Username correctly', max_length=250)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))

    


class NewPhotoBlog(forms.Form):
    title = forms.CharField(label='Enter your Username correctly', max_length=250)
    photo = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))



class NewAudioBlog(forms.Form):
    title = forms.CharField(label='Enter your Username correctly', max_length=250)
    audio = forms.FileField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))



class NewVideoBlog(forms.Form):
    title = forms.CharField(label='Enter your Username correctly', max_length=250)
    video = forms.FileField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))



#forms for sign up 

class BloggerUserSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'surname', 'email', 'profile_picture', 'password1', 'password2']

    def save(self, commit =True):
        user = super().save(commit=False)
        user.is_blogger = True

        if commit:
            user.save()
        return user
        


class RegularUserSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'surname', 'email', 'profile_picture', 'password1', 'password2']

    def save(self, commit =True):
        user = super().save(commit=False)
        user.is_blogger = False

        if commit:
            user.save()
        return user
    

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'bio', 'profile_picture']  # Fields to edit

    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write something about yourself...'}), required=False)

#forms for login




class CustomLoginForm(AuthenticationForm):
    pass
        
