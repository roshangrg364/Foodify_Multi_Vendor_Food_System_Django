from django import forms
from .models import vendor
from accounts.validations import validate_images


class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[validate_images],
    )

    class Meta:
        model = vendor
        fields = ["vendor_name", "vendor_license"]
