from django.forms import ModelForm

from blog.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        labels = {
            "email": "Your email:",
            "author": "Name:",
        }
        fields = ["author", "email", "message"]
