from django import forms
from .models import ContactUsMessage


class ContactUsMessageForm(forms.ModelForm):
    
    class Meta:
        model = ContactUsMessage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs.update({
                "placeholder":f"{f.title()}"
            })

