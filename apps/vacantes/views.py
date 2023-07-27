from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PerfilForm
from .models import Vacante, Area, Perfil, Postulados
from django.contrib import messages
from django.db.models import Q
# from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template

from django.utils.html import strip_tags

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class Home(View):

    nav = "../components/NavMain.html"
    menu_areas = "../components/MenuAreas.html"
    perfil = "../components/Perfil.html"
    filter = "../components/FilterPage.html"

    def get(self, request):

        vacante = Vacante.objects.filter(visible=True)
        postulados = Postulados.objects.filter(usuario=request.user)

        print(postulados)

        template_name = "layouts/home.html"
        context = {
            "menu_areas": self.menu_areas,
            "perfil": self.perfil,
            "nav": self.nav,
            "filter": self.filter,
            "postulados": postulados,
            "nav_data": [
                {"url": "home", "title": "Página principal"},
                {"url": "perfil", "title": "Perfil"},
                {"url": "logout", "title": "Cerra sesión"},
            ],
            "vacantes": vacante,
        }

        return render(request, template_name, context)

class HomeFiltered(View):

    nav = "../components/NavMain.html"
    menu_areas = "../components/MenuAreas.html"
    perfil = "../components/Perfil.html"
    filter = "../components/FilterPage.html"

    def get(self, request, area):
        area_obj = Area.objects.get(area=area)
        vacante = Vacante.objects.filter(area=area_obj)
        postulados = Postulados.objects.filter(usuario=request.user)
        template_name = "layouts/home.html"
        context = {
            "menu_areas": self.menu_areas,
            "perfil": self.perfil,
            "nav": self.nav,
            "filter": self.filter,
            "postulados": postulados,
            "nav_data": [
                {"url": "home", "title": "Página principal"},
                {"url": "perfil", "title": "Perfil"},
                {"url": "logout", "title": "Cerra sesión"},
            ],
            "vacantes": vacante,
        }

        return render(request, template_name, context)

def BorrarVacante(request, id):
    
    postulado = Postulados.objects.get(id=id)

    user = User.objects.get(username=request.user)
    first_name = user.first_name
    last_name = user.last_name

    name = first_name + " " + last_name

    # subject = 'Vacante cancelada'
    # message = render_to_string('email_template.html', {'message': postulado, 'name': name})
    # from_email = settings.EMAIL_HOST_USER
    # recipient_list = ['marcovazqueznoriega41@gmail.com']
    # text_content = strip_tags(message)
    # email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    # email.attach_alternative(message, "text/html")
    # email.send()

    postulado.delete()
    
    return redirect('home')

class FullVacante(View):

    template_name = "layouts/full_vacante.html"
    nav = "../components/NavMain.html"

    def get(self, request, vacante):
        vacante = Vacante.objects.get(slug=vacante)
        print("------")
        print(vacante)
        context = {
            "nav": self.nav,
            "nav_data": [
                {"url": "home", "title": "Página principal"},
                {"url": "perfil", "title": "Perfil"},
                {"url": "logout", "title": "Cerra sesión"},
            ],

            "vacante": vacante
        }

        return render(request, self.template_name, context)

    def post(self, request, vacante):
        usuario = request.user
        vacante = vacante

        first_name = usuario.first_name
        last_name = usuario.last_name

        name = first_name + " " + last_name

        data_send = Perfil.objects.filter(Q(nombre=name))

        
        validate = Postulados.objects.filter(Q(usuario=usuario) & Q(vacante=vacante))



        if validate:
            
            messages.error(request, "No puedes postularte otra vez")

            return redirect('home')
        
        else:

            data = Postulados( usuario=usuario, vacante=vacante )

            data.save()



            # subject = 'Vacante nueva'
            # message = render_to_string('correo.html', {'message': data_send, "vacante": vacante})
            # from_email = settings.EMAIL_HOST_USER
            # recipient_list = ['marcovazqueznoriega41@gmail.com']
            # text_content = strip_tags(message)
            # email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
            # email.attach_alternative(message, "text/html")
            # email.send()

            messages.success(request, "Te has postulado con exito")

            return redirect('home')

            


class MiPerfil(View):

    template_name = "layouts/perfil.html"
    nav = "../components/NavMain.html"



    def get(self, request):

        user = User.objects.get(username=request.user)
        first_name = user.first_name
        last_name = user.last_name
        
        name = first_name + " " + last_name

        print(name)
        
        form = PerfilForm

        context = {
            "form": form,
            "nav": self.nav,
            "nav_data": [
                {"url": "home", "title": "Página principal"},
                {"url": "perfil", "title": "Perfil"},
                {"url": "logout", "title": "Cerra sesión"},
            ],
            "name": name
        }

        return render(request, self.template_name, context)

    def post(self, request):

        nombre = request.POST['nombre']
        carrera = request.POST['carrera']
        genero = request.POST['genero']
        experiencia = request.POST['experiencia']
        
        data = Perfil(
            nombre = nombre,
            carreras = carrera,
            genero = genero,
            experiencia = experiencia
        )

        data.save()

        return redirect('home')
