from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")
        labels = {
            "username": "닉네임",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
        }
