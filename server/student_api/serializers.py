from student_api.models import StudentModel
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['id', 'name', 'area', 'rows','email', 'validated']
    """
    def create(self, validated_data):
         return StudentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance """