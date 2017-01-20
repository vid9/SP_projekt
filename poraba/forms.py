from django import forms
from .models import Specifikacije, Znamka, Car

class LoginForm(forms.Form):
  username = forms.CharField(label='',
                             validators=[],
                             widget = forms.TextInput(
                                 attrs={"type": "text",
                                        "placeholder": "Uporabniško ime",
                                        "name": "uname",
                                        "required": "required",
                                        "class": "podatki" }
                                )
                             )
  password =  forms.CharField(label='',
                             validators=[],
                             widget = forms.TextInput(
                                 attrs={"type": "password",
                                        "placeholder": "Geslo",
                                        "name": "uname",
                                        "required": "required",
                                        "class": "podatki" }
                                )
                             )

#
# class ZnamkaForm(forms.ModelForm):
#     znamka =  forms.CharField(label='',
#                              validators=[],
#                              widget = forms.TextInput(
#                                  attrs={"type": "text",
#                                         "placeholder": "Znamka avtomobila",
#                                         "id": "znamka",
#                                         "required": "required",
#                                         "class": "podatki" }
#                                 )
#                              )
#
#     class Meta:
#         model = Znamka
#         fields = ['znamka']
#
# class SerijaForm(forms.ModelForm):
#     serija = forms.CharField(label='',
#                              validators=[],
#                              widget=forms.TextInput(
#                                  attrs={"type": "text",
#                                         "placeholder": "Serija avtomobila",
#                                         "id": "serija",
#                                         "required": "required",
#                                         "class": "podatki"}
#                              )
#                              )
#
#

class SpecifikacijeForm(forms.Form):
    znamka = forms.CharField(label='',
                               validators=[],
                               widget = forms.TextInput(
                                   attrs={"type": "text",
                                          "placeholder": "Znamka avtomobila",
                                          "id": "znamka",
                                          "required": "required",
                                          "class": "podatki" }
                                  )
                               )
    model = forms.CharField(label='',
                             validators=[],
                             widget=forms.TextInput(
                                 attrs={"type": "text",
                                        "placeholder": "Model avtomobila",
                                        "id": "model",
                                        "required": "required",
                                        "class": "podatki"}
                                )
                             )
    visina = forms.IntegerField(label='',
                             validators=[],
                             widget=forms.TextInput(
                                 attrs={"type": "number",
                                        "placeholder": "Višina avtomobila (mm)",
                                        "id": "visina",
                                        "required": "required",
                                        "class": "podatki"}
                                )
                             )
    dolzina = forms.IntegerField(label='',
                             validators=[],
                             widget=forms.TextInput(
                                 attrs={"type": "number",
                                        "placeholder": "Dolžina avtomobila (mm)",
                                        "id": "dolzina",
                                        "required": "required",
                                        "class": "podatki"}
                                )
                             )
    tip = forms.CharField(label='',
                              validators=[],
                              widget=forms.TextInput(
                                  attrs={"type": "text",
                                         "placeholder": "Dizel/Bencin",
                                         "id": "tip",
                                         "required": "required",
                                         "class": "podatki"}
                                )
                              )
    vtanka = forms.IntegerField(label='',
                              validators=[],
                              widget=forms.TextInput(
                                  attrs={"type": "number",
                                         "placeholder": "Velikost rezervoarja (l)",
                                         "id": "rezervoar",
                                         "required": "required",
                                         "class": "podatki"}
                                )
                              )
    # imgfile = forms.ImageField(label='Choose your image',
    #
    #                          help_text='The image should be cool.')
    # class Meta:
    #     model = Specifikacije
    #     fields = ['visina', 'dolzina','tip','vtanka','poraba']

class RegistrationForm(forms.Form):
    username = forms.CharField(validators=[],
                             widget = forms.TextInput(
                                 attrs={ "class": "podatki",
                                         "name": "username",
                                        "id": "username",
                                        "type": "text",
                                        "placeholder": "Uporabniško ime",
                                        "required": "required"}
                                )
                             )
    first_name = forms.CharField(validators=[],
                             widget=forms.TextInput(
                                 attrs={"class": "podatki",
                                        "name": "name",
                                        "id": "first_name",
                                        "type": "text",
                                        "placeholder": "Ime"}
                             )
                             )
    last_name = forms.CharField(validators=[],
                             widget=forms.TextInput(
                                 attrs={"class": "podatki",
                                        "name": "last",
                                        "id": "last_name",
                                        "type": "text",
                                        "placeholder": "Priimek"}
                             )
                             )
    password = forms.CharField(label='',
                             validators=[],
                             widget = forms.TextInput(
                                 attrs={"type": "password",
                                        "placeholder": "Geslo",
                                        "name": "uname",
                                        "required": "required",
                                        "class": "podatki" }
                                )
                             )
    email = forms.EmailField(validators=[],
                             widget = forms.TextInput(
                                 attrs={ "class": "podatki",
                                         "name": "email",
                                        "id": "email",
                                        "type": "email",
                                        "placeholder": "Email",
                                        "required": "required"}
                                )
                             )


def get_my_choices():
    context = {}
    # context['model'] = Car.objects.filter("model").distinct()
    l=[(o.id, o.model) for o in Car.objects.all()]

    # l = Car.objects.values("model").distinct()
    print(list(l))
    return list(l)

class PorabaForm(forms.Form):

    """
    def __init__(self, *args, **kwargs):
        super(PorabaForm, self).__init__(*args, **kwargs)
        self.fields['avto'] = forms.ChoiceField(choices=get_my_choices(), widget=forms.Select(attrs={"size": "3", "class": "options-profil third", "value": "0"}
                                                 )
                            )
    """
    avto = forms.ChoiceField(validators=[],
                             choices=get_my_choices(),
                             widget=forms.Select(attrs={"size": "3", "class": "options-profil third"}
                                                 )
                            )
    poraba = forms.DecimalField(validators=[],
                                widget=forms.TextInput(attrs={"type": "number",
                                                              "name": "poraba",
                                                              "step": "0.1",
                                                              "class": "podatki",
                                                              "style": "margin-left: 20px",
                                                              "value": "6.0",
                                                                }
                                                       )
                                )