from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from muevelasnalgas.models import TipoZona, Zona
from urllib.parse import quote, unquote

@login_required
def mapaView(request):
    zonas = Zona.objects.all()
    tipos = TipoZona.objects.all()
    buscar = ""
    if "buscar" in request.GET:
        buscar = request.GET["buscar"]
        if buscar == "":
            return HttpResponseRedirect("../../deportivas")
        zonas = zonas.filter(Q(nombre__icontains=buscar) | Q(descripcion__icontains=buscar) | Q(tipo__nombre__icontains=buscar))
    return render(request, 'mapa.html', context={'zonas':zonas,
                                                 'tipos':tipos,
                                                 'filtro':buscar})