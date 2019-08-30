from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("User not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("User no longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label="Email Address",widget=forms.EmailInput(attrs={'autocomplete':'on','placeholder':'Email inpu'}))
	email2 = forms.EmailField(label="Confirm Email")
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = (
				'username',
				'email',
				'email2',
				'password',
			)

			
	# def clean(self, *args, **kwargs):
	# 	email = self.cleaned_data_get('email')
	# 	email2 = self.cleaned_data_get('email2')
	# 	if email != email2:
	# 		raise forms.validationError("Email Must be same")
	# 	email_qs = User.objects.filter(email=email)
	# 	if email_qs.exists():
	# 		raise forms.ValidationError("Email already register")
	# 	return super(UserRegisterForm,self).clean(*args, **kwargs)	

##########...... OR ........##########

	def clean_email2(self):
		print(self.cleaned_data)
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Email Must be same")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email already register")
		return email

