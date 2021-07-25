from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task, UserProfile


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control form-control-lg flex-column  col-5 ', 'id': 'input-form'})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'id':'floatingInput', 'placeholder': 'Enter Username' 
            })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'id':'floatingPassword', 'placeholder':'Enter password'
            })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'id':'floatingPassword2', 'placeholder': 'Confrim Password '
            })

class ProfileCreationForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control', 'id':'floatingInput', 'placeholder': 'Enter Firstname' 
            })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control', 'id':'floatingInput2', 'placeholder': 'Enter Firstname' 
            })
        self.fields['dark_mode'].widget.attrs.update({
            'class': 'form-check-input bg-secondary bg-outline-dark', 'id': 'exampleCheck1',
            })
