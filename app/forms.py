from django import forms
from django.core import validators

def validate_for_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError('First Letter Should not be "a"')

def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('Length is Less Than 5')

    
class StudenForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    Sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        em=self.cleaned_data['email']
        rem=self.cleaned_data['remail']

        if em != rem:
            raise forms.ValidationError('Emails is not Matching')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('Bot is Inserting the Data')
