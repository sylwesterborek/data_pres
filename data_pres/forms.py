from django.forms import ModelForm, Textarea
from .models import Dane

class DanesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)
        self.fields['teryt'].widget.attrs.update({'class': 'form-control'})
        self.fields['okres'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana1'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana2'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana3'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana4'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana5'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana6'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana7'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana8'].widget.attrs.update({'class': 'form-control'})
        self.fields['dana9'].widget.attrs.update({'class': 'form-control'})
        #self.fields['watchAgain'].widget.attrs.update(\
        #    {'class': 'form-check-input'})
    class Meta:
        model = Dane
        fields = ['teryt','okres','dana1','dana2','dana3','dana4',\
            'dana5','dana6','dana7','dana8','dana9']
        # labels = {\
        #     'watchAgain': ('Watch Again')
        # }
        # widgets = {
        #     'text': Textarea(attrs={'rows': 4}),
        # }    