from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('full_name')  # Assign full name to the first_name field
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone_number', 'appointment_date',
                  'session_type', 'additional_notes', 'amount', 'uploaded_image']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }
