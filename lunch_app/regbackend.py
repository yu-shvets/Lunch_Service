from registration.backends.simple.views import RegistrationView
from .forms import ProfileForm
from .models import UserProfile


class MyRegistrationView(RegistrationView):

    form_class = ProfileForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        phone = form_class.cleaned_data['phone']
        new_profile = UserProfile.objects.create(user=new_user, phone=phone)
        new_profile.save()

        return new_user


