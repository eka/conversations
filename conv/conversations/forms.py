from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)


class ConversationForm(forms.Form):
    title = forms.CharField(max_length=70)


class ConversationMessageForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput, max_length=255)
