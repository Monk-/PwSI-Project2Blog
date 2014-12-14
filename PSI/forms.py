from django import forms
from blog.models import UserProfile, Category, Post
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField ,User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )


class CommentForm(forms.Form):
    body = forms.CharField(label='', required=True,
    error_messages={'required': 'Empty!!'})

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'content', 'categories')
# class PostForm(forms.Form):
#     categories = forms.CharField(choices=Category)
#     title = forms.CharField(max_length=65)
#     description = forms.TextField(max_length=155)
#     content = forms.TextField()



#
# class CommentForm(forms.Form):
#     body = forms.CharField(label='Write something here:', required=True,
#     error_messages={'required': 'You cannot put empty comment! : )'})




