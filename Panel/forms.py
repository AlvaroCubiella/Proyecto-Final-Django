class LoginForm():
    user = forms.CharField(label = 'Username ', max_length = 25)
    pwd  = forms.CharField(label = 'Password ', widget =  forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None # You need to make the user as None initially
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(userLogin, self).clean()
        user         = cleaned_data.get("user")
        pwd          = cleaned_data.get("pwd")

        # Now you get the user
        self.user_cache = authenticate(username=user, password=pwd)
        # Do other stuff
        return self.cleaned_data

    # Function to return user in views
    def get_user(self):
        return self.user_cache     