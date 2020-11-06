from django import forms


class Loginform(forms.Form):
    username=forms.CharField(max_length=100,label='username')
    password=forms.CharField(max_length=100,label="password",widget=forms.PasswordInput())


class Signupform(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=100, label="Confirm password",widget=forms.PasswordInput())
    dateofbirth = forms.DateField(label="date of birth" ,widget=forms.DateInput(),initial="1981-02-19")
    phoneno = forms.CharField(max_length=15, label="phone no",widget=forms.NumberInput())
    profileimage = forms.ImageField( label="profile image ",widget=forms.FileInput())
    email = forms.EmailField(label="email ", widget=forms.EmailInput())


class Updateform(forms.Form):
    username = forms.CharField(max_length=100, label='username',disabled=True)
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=100, label="Confirm password",widget=forms.PasswordInput())
    dateofbirth = forms.DateField(label="date of birth" ,widget=forms.DateInput(),initial="1981-02-19")
    phoneno = forms.CharField(max_length=15, label="phone no",widget=forms.NumberInput())
    profileimage = forms.ImageField( label="profile image ",widget=forms.FileInput())
    email = forms.EmailField(label="email ", widget=forms.EmailInput())