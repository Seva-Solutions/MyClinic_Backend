from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *
import geopy.distance
from django.contrib.gis.geoip2 import GeoIP2

@api_view(['GET',])
def total_clinics(request):

    clinic_view = None
    try:
        clinic_view = Clinic.objects.all().count()
    except Patient.DoesNotExist:
        return Response(f'Clinics do not exist', status=404)

    if request.method == "GET":
        clinic_view = Clinic.objects.all().count()

    return Response(clinic_view, status=status.HTTP_200_OK)

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def clinics(request):

    if request.method == "GET":
        clinic_view = None
        try:
            clinic_view = Clinic.objects.get(id=id)
        except Clinic.DoesNotExist:
            return Response(f'Clinic does not exist', status=404)
        serializer = ClinicSerializer(clinic_view,many=True)
    elif request.method == 'POST':
        add_clinic = None
        serializer = ClinicSerializer(add_clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Clinic Sucessfully Added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST',])
@permission_classes([IsAuthenticated])
@csrf_exempt
def nearby_clincs(request, id):

    if request.method != 'POST':
        return HttpResponse('Only the POST verb can be used on this endpoint.', status=405)
    
    clinics = None
    clinics_list = []
    requestJson = json.loads(request.body)
    patientLoc = getGeoLocation(request)
    patientLatitude = requestJson.get('lat', patientLoc[0])
    patientLongitude = requestJson.get('long', patientLoc[1])
    radius = requestJson.get('radius', 15)

    for clinic in clinics:
        clinicLatitude = float(clinic.clinicLatitude)
        clinicLongitude = float(clinic.clinicLongitude)

        distance = getMeterDistanceBetweenTwoLocations(patientLatitude, patientLongitude, clinicLatitude, clinicLongitude)
        if distance <= radius:
            serializer = ClinicSerializer(clinic)
            clinics_list = append(serializer.data)
    
    return JsonResponse({'nearby clinics': clinics_list})

def getGeoLocation(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2()
    return g.lat_lon(str(ip))

def getMeterDistanceBetweenTwoLocations(lat1, long1, lat2, long2):
    coords_1 = (lat1, long1)
    coords_2 = (lat2, long2)
    return geopy.distance.distance(coords_1, coords_2).km
