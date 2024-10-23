from django import forms
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'location', 'capture_date']
        widgets = {
            'capture_date': forms.SelectDateWidget(years=range(2000, 2030)),
        }

class PhotoSearchForm(forms.Form):
    location = forms.CharField(required=False, label='Location')
    start_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(2000, 2030)), label='Start Date')
    end_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(2000, 2030)), label='End Date')