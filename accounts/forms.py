from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomeUserCrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','age')#UserCreationForm.Meta.fields + ('age',) #'__all__'

class CustomeUserChageForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age')#UserChangeForm.Meta.fields