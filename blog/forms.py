from django import forms

class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"type":"email", "id":"semail", "name":"semail1", "class":"form-control mr-md-1 semail", "placeholder":"Enter email"}))

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(attrs={
            "class":" form-control","placeholder":"Your Name"
            })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=60, 
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
            }))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"form-control","type":"email","placeholder":"Your Email"}))
    
    body = forms.CharField(max_length=10000, 
            widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Send me a message"}))
