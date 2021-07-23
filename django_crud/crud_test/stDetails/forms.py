from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name', 'email', 'password']
        #we have created our form, go to view and pass this form to the template    
        # adding widgets
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
        # render_values password to database se nikal ke form me show krne me help krta hai        
