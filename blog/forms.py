from django import forms

from captcha.fields import CaptchaField


class CommentForm(forms.Form):
    author = forms.CharField(max_length=23)
    message = forms.CharField(widget=forms.Textarea, max_length=900)
    captcha = CaptchaField()
