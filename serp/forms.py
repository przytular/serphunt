from django import forms

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, HTML
from crispy_forms.bootstrap import FieldWithButtons
from allauth.account.forms import LoginForm

from .models import UserConfig, SearchResults


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


class HistoryForm(forms.Form):
	requests = forms.ModelChoiceField(queryset=SearchResults.objects.none(), required=False)

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'history'
		self.helper.form_action = reverse_lazy('keywords-list')
		self.fields['requests'].queryset = SearchResults.objects.filter(user=user)


class UserConfigForm(forms.ModelForm):
	class Meta:
		model = UserConfig
		fields = ['time_limit', 'user_agent']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'config'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse_lazy('config')
		self.helper.layout = Layout(
			Field('time_limit'),
			Field('user_agent'),
			Submit("submit", "Save", css_class='btn-primary')
		)
		self.fields['time_limit'].label = 'Scraper time limit for the same keyword (in seconds)'
		self.fields['user_agent'].required = False


class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # Add magic stuff to redirect back.
        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
            )
        )
        # Add submit button like in original form.
        self.helper.layout.append(
            HTML(
                '<button class="btn btn-primary btn-block" type="submit">'
                '%s</button>' % _('Sign In')
            )
        )
