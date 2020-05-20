from rest_framework import serializers

from .models import Lesson, Teacher

class TeacherSerializer(serializers.ModelSerializer):
    short_name = serializers.CharField()
    name = serializers.CharField()
    position = serializers.CharField()
    imageUrl = serializers.FileField(source='image')

    class Meta:
        model = Teacher
        exclude = ('id', 'image',)


class LessonsSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    startTime = serializers.TimeField(format='%H.%M')
    endTime = serializers.TimeField(format='%H.%M')
    weekDay = serializers.SlugRelatedField(slug_field='id', read_only=True)    
    teacher_v2 = TeacherSerializer()    
    availability = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'place', 'teacher', 'startTime', 'endTime', 'weekDay', 'appointment_id',
                 'service_id', 'pay', 'appointment', 'teacher_v2', 'color', 'availability')

    def get_teacher(self, obj):
        return obj.teacher_v2.short_name
