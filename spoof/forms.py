from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, HTML


class AddProxiesForm(forms.Form):
	new_proxies = forms.CharField(label='Add new proxies', widget = forms.Textarea())

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'proxies'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse_lazy('proxies-list')
		self.helper.layout = Layout(
			Field('new_proxies'),
			Submit("submit", "Add", css_class='btn-primary')
		)
