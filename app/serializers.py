from rest_framework import serializers

from .models import Project 
#nombre del modelo creado o tabla creada en la db


class ProjectSerializer(serializers.ModelSerializer):  #clase cualquier nombre, hereda, 
#convierte un modelo en datos que pueden ser consultados

    class Meta:
        model = Project  #el modelo a consultar en db
        fields = '__all__' #los campos que son consultados    = ('id', 'title'...)

        read_only_fields = ('created_at',) #que campo son de solo lectura, no se puede editar, tiene que llevar una coma
        
