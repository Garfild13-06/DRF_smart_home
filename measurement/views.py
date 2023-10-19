from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorView(ListAPIView):
    # стандартный запрос информации обо всех датчиках через GET
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        # добавление нового датчика через POST
        name = request.GET.get('name', '')
        description = request.GET.get('description', '')
        try:
            if name == '':
                return Response({'status': 'Error: Empty name'})
            else:
                Sensor(name=name, description=description).save()
                return Response({'status': 'OK'})
        except:
            return Response({'status': 'add failed'})

    def patch(self, request):
        # изменение данных датчика через PATCH
        sensor_id = request.GET.get('id', '')
        name = request.GET.get('name', '')
        description = request.GET.get('description', '')
        sensor = Sensor.objects.get(id=sensor_id)
        if name == '':
            return Response({'status': 'Error: Empty name'})
        elif sensor.name == name and sensor.description == description:
            return Response({'status': 'Error: new values are the same as old'})
        else:
            sensor.name = name
            sensor.description = description
            sensor.save()
            return Response({'status': 'OK'})


class MeasurementView(ListAPIView):
    # стандартный запрос информации обо всех измерениях через GET
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        # добавление измерений через POST
        sensor_id = request.GET.get('sensor_id', 0)
        temperature = request.GET.get('temperature', 0)
        if sensor_id == 0:
            return Response({'status': 'Error: Не указан датчик'})
        elif int(sensor_id) > 0:
            Measurement(sensor_id_id=sensor_id, temperature=temperature).save()
            return Response({'status': 'OK'})
        else:
            return Response({'status': 'add failed'})


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
