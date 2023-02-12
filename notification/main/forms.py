from django import forms
from phonenumber_field.formfields import PhoneNumberField


class SubmitForm(forms.Form):
    first_name = forms.CharField(
        label='First Name', max_length=100, validators=[], 
        widget=forms.TextInput(attrs={
            "placeholder": "First Name", "class": "form-control"}))
    last_name = forms.CharField(
        label='Last Name', max_length=100, validators=[], 
        widget=forms.TextInput(attrs={
            "placeholder": "Last Name", "class": "form-control"}))
    mobile_no = PhoneNumberField(
        label='Mobile No.', validators=[], 
        widget=forms.TextInput(attrs={
            "placeholder": "+919999999999", "class": "form-control"}))
    notification_time = forms.DateTimeField(
        label='Notification Time', validators=[],
        widget=forms.DateTimeInput(attrs={
            "placeholder": "%Y-%m-%d %H:%M", "class": "form-control"}))