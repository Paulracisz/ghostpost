from django import forms


class AddPostForm(forms.Form):
    description = forms.CharField(max_length=280)
    CHOICES = [(True, 'Roast'),(False ,'Boast')]
    r_bool = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES)