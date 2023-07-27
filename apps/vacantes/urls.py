from django.urls import path
from .views import Home, FullVacante, MiPerfil, HomeFiltered, BorrarVacante

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("vacante/<str:vacante>", FullVacante.as_view(), name="vacante"),
    path("vacantes/<str:area>", HomeFiltered.as_view(), name="filter"),
    path("perfil/", MiPerfil.as_view(), name="perfil"),
    path("delete/<int:id>/", BorrarVacante, name="delete")
]