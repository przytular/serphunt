from django import forms

from django.urls import reverse_lazy
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from crispy_forms.bootstrap import FieldWithButtons

from .models import UserConfig


class SearchForm(forms.Form):
	keyword = forms.CharField()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'search'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse_lazy('keywords-list')
		self.helper.form_show_labels = False
		self.helper.layout = Layout(
			FieldWithButtons('keyword', Submit("submit", "Hunt!", css_class='btn-danger'))
		)


class UserConfigForm(forms.ModelForm):
	class Meta:
		model = UserConfig
		fields = ['time_limit']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'config'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse_lazy('config')
		self.helper.layout = Layout(
			Field('time_limit'),
			Submit("submit", "Save", css_class='btn-primary')
		)
		self.fields['time_limit'].label = 'Scraper time limit for the same keyword (in seconds)'