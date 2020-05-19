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
    name = serializers.CharField()
    description = serializers.CharField()
    place = serializers.CharField()
    teacher = serializers.SerializerMethodField()
    startTime = serializers.TimeField(format='%H.%M')
    endTime = serializers.TimeField(format='%H.%M')
    weekDay = serializers.SlugRelatedField(slug_field='id', read_only=True)
    appointment_id = serializers.CharField()
    service_id = serializers.CharField()
    pay = serializers.BooleanField()
    appointment = serializers.BooleanField()
    teacher_v2 = TeacherSerializer()
    color = serializers.CharField()
    availability = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Lesson
        exclude = ('id',)

    def get_teacher(self, obj):
        return obj.teacher_v2.short_name
