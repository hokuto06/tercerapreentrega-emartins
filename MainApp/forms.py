from django import forms

class AccessPointForm(forms.Form):

    deviceName = forms.CharField()
    ipAddress = forms.GenericIPAddressField()
    status = forms.IntegerField()

class SwitchForm(forms.Form):

    deviceName = forms.CharField()
    ipAddress = forms.GenericIPAddressField()
    status = forms.IntegerField()
    marca = forms.CharField()    