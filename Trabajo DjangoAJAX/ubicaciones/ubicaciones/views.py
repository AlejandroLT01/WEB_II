from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Estado, Municipio

def form_view(request):
    estados = Estado.objects.all().order_by('nombre')
    return render(request, 'ubicaciones/formulario.html', {'estados': estados})

def get_municipios(request):
    if request.method != 'GET':
        return HttpResponseBadRequest("Método no permitido")

    estado_id = request.GET.get('estado_id')
    if not estado_id:
        return JsonResponse({'error': 'estado_id requerido'}, status=400)

    municipios_qs = Municipio.objects.filter(estado_id=estado_id).order_by('nombre').values('id', 'nombre')
    municipios = list(municipios_qs)
    return JsonResponse({'municipios': municipios})
