from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from muevelasnalgas.models import Comunidad, Noticia

@login_required
def comunidadesView(request):
    noticias = Noticia.objects.all().order_by('-id')[:5]
    comunidades = Comunidad.objects.all()
    if "buscar" in request.GET:
        comunidades = comunidades.filter(nombre__contains=buscar)
        comunidades.union(comunidades.filter(deporte__nombre__contains=buscar))
    top = Comunidad.objects.annotate(num_miebros=Count('miembros')).order_by('num_miebros')[:3]
    return render(request, 'comunidades.html', context={'noticias':noticias,
                                                        'comunidades':comunidades,
                                                        'top':top})

@login_required
def comunidadesMiembro(request, **kwargs):
    id = kwargs.get("id")
    comunidad = Comunidad.objects.get(id=id)
    if request.user in comunidad.miembros.all():
        comunidad.miembros.remove(request.user)
        comunidad.save()
        if request.user in comunidad.favoritos.all():
            comunidad.favoritos.remove(request.user)
            comunidad.save()
    else:
        comunidad.miembros.add(request.user)
        comunidad.save()
    return HttpResponseRedirect("../../comunidades")

@login_required
def comunidadesFavorito(request, **kwargs):
    id = kwargs.get("id")
    comunidad = Comunidad.objects.get(id=id)
    if request.user in comunidad.favoritos.all():
        comunidad.favoritos.remove(request.user)
        comunidad.save()
    else:
        comunidad.favoritos.add(request.user)
        comunidad.save()
        if not request.user in comunidad.miembros.all():
            comunidad.miembros.add(request.user)
            comunidad.save()
    return HttpResponseRedirect("../../comunidades")