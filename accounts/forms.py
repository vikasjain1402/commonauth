from django import forms


class Loginform(forms.Form):
    username=forms.CharField(max_length=100,label='username')
    password=forms.CharField(max_length=100,label="password",widget=forms.PasswordInput())


class Signupform(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=100, label="Confirm password",widget=forms.PasswordInput())
    dateofbirth = forms.DateField(label="date of birth" ,widget=forms.DateInput(),initial="1981-02-19")
    phoneno = forms.CharField(max_length=15, label="phone no",widget=forms.NumberInput(),initial=9810955544)
    profileimage = forms.ImageField( label="profile image ",widget=forms.FileInput())
    email = forms.EmailField(label="email ", widget=forms.EmailInput(),initial="vikas@gmail.com")


class Updateform(forms.Form):
    username = forms.CharField(max_length=100, label='username',disabled=True,required=False)
    password = forms.CharField(max_length=100, label="password", widget=forms.PasswordInput(),required=False)
    cpassword = forms.CharField(max_length=100, label="Confirm password",widget=forms.PasswordInput(),required=False)
    dateofbirth = forms.DateField(label="date of birth" ,widget=forms.DateInput(),initial="1981-02-19",required=False)
    phoneno = forms.CharField(max_length=15, label="phone no",widget=forms.NumberInput(),required=False)
    profileimage = forms.ImageField( label="profile image ",widget=forms.FileInput(),required=False)
    email = forms.EmailField(label="email ", widget=forms.EmailInput(),required=False)