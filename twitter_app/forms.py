from django.forms import ModelForm
from .models import Tweet


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = "__all__"
