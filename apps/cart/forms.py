from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="Cantidad", widget=forms.NumberInput(attrs={
        'class':'form-control',
        'value':'1'
    }))
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
