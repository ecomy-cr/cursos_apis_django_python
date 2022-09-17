#archivo con los viewset
#importo mi models

from .models import Project

from rest_framework import viewsets, permissions 
from .serializers import ProjectSerializer



class ProjectViewSet(viewsets.ModelViewSet):  #clase que hereda de django rest frame
  queryset = Project.objects.all() #consultamos todos los objetos, todas las columnas de la table db

  permission_classes = [permissions.AllowAny] #los permisos para las consultas: allowany cualquier cliente puede solicitar datos a mi servidor 
  #aqui mas adelante esta ( is athentic ) por si esta login o no esta login el usuario ejemplo.



  serializer_class = ProjectSerializer  #mis datos legibles por el serializer, como los voy a convertir
