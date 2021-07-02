from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.db.models.fields import FloatField
from django.forms.fields import FloatField as FloatFormField
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from muevelasnalgas.models import TipoZona, Zona
from urllib.parse import quote, unquote

@login_required
def mapaView(request):
    zonas = Zona.objects.all()
    tipos = TipoZona.objects.all()
    buscar = ""
    cercanos = ""
    if "checkCercanos" in request.GET and "lat" in request.GET and "lng" in request.GET:
        cercanos = request.GET["checkCercanos"]
        model_field = FloatField()
        form_field = model_field.formfield(localize=True)
        lat = form_field.to_python(request.GET["lat"].replace('.',','))
        lng = form_field.to_python(request.GET["lng"].replace('.',','))
        lejos = []
        for zona in zonas:
            if abs(zona.lat - lat) > 0.03:
                lejos.append(zona.id)
            elif abs(zona.lng - lng) > 0.03:
                lejos.append(zona.id)
        zonas = zonas.exclude(id__in=lejos)
        print(lejos)
    if "buscar" in request.GET:
        buscar = request.GET["buscar"]
        if buscar == "" and "checkCercanos" not in request.GET:
            return HttpResponseRedirect("../../deportivas")
        zonas = zonas.filter(Q(nombre__icontains=buscar) | Q(descripcion__icontains=buscar) | Q(tipo__nombre__icontains=buscar))
    
    return render(request, 'mapa.html', context={'zonas':zonas,
                                                 'tipos':tipos,
                                                 'filtro':buscar,
                                                 'cercanos':cercanos})

@login_required
@require_POST
@csrf_exempt
def getZonas(request):
    buscar = request.POST["buscar"]
    cercanos = request.POST["cercanos"]
    model_field = FloatField()
    form_field = model_field.formfield(localize=True)
    lat = form_field.to_python(request.POST["lat"].replace('.',','))
    lng = form_field.to_python(request.POST["lng"].replace('.',','))
    zonas = Zona.objects.all().filter(Q(nombre__icontains=buscar) | Q(descripcion__icontains=buscar) | Q(tipo__nombre__icontains=buscar))
    lejos = []
    for zona in zonas:
        if abs(zona.lat - lat) > 0.03:
            lejos.append(zona.id)
        elif abs(zona.lng - lng) > 0.03:
            lejos.append(zona.id)
    zonas = zonas.exclude(id__in=lejos)
    return JsonResponse(list(zonas.values('nombre')), safe=False)

