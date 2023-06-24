from django import forms
from .models import Fruits

class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = ('name', 'image_url', 'description', 'nutrition')
        widgets = {
            'name': forms.TextInput(attrs = {'placeholder': 'First Name'}),
            'image_url': forms.TextInput(attrs = {'placeholder': 'Fruit Image URL'}),
            'description': forms.TextInput(attrs = {'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs = {'placeholder': 'Nutrition Info'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label = False

class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = ('name', 'image_url', 'description', 'nutrition')

class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = ('name', 'image_url', 'description', 'nutrition')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'