from .models import user,users,doctor,us,us2,cust
from  rest_framework import serializers

class jsonuser(serializers.ModelSerializer):
    class Meta:
        model=user
        fields= '__all__'


class jusers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'


class doctor_j(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = '__all__'


class us_j(serializers.ModelSerializer):
    class Meta:
        model = us
        fields = '__all__'


class us2_j(serializers.ModelSerializer):
    class Meta:
        model = us2
        fields = ('id',
                  'name',
                  'city',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = cust
        fields = ('id',
                  'name',
                  'city',  )