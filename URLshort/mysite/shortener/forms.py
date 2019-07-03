from django import forms
from django.core.validators import URLValidator

#def validate_dot_com(value):
 #   if not ".com" or ".ca" or ".org" or".edu":
  #      raise forms.ValidationError('Please Input a valid URL')
    
class SubmitURLForm(forms.Form):
    url = forms.CharField(label='Input Url')

    def clean(self):
        cleaned_data= super(SubmitURLForm, self).clean()
        url = cleaned_data.get('url')

        if url==None:
            url='NoURL'
        else:
            url=url

        if '.com' in url:
            pass;

        elif '.ca' in url:
            pass;

        elif '.gov' in url:
            pass;

        elif '.edu' in url:
            pass;

        elif '.org' in url:
            pass;

        else:
            raise forms.ValidationError('Please Input a valid URL')
            
        url_validator=URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError('Please Input a valid URL')
        return url
