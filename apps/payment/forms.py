from django import forms
from .models import BillingAddress

class BillingAddressForm(forms.ModelForm):
    
    class Meta:
        model = BillingAddress
        fields = "__all__"
        exclude=['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs.update({
                "placeholder": self.fields[f].label,
                "class":"input",
            })


