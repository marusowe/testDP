from rest_framework import serializers

from urlshort_api.models import UrlShort


class UrlShortCreateSerializer(serializers.ModelSerializer):
    custom_hash = serializers.CharField(max_length=128, required=False)

    class Meta:
        model = UrlShort
        fields = ('full_url', 'hash', 'short_url', 'custom_hash')
        extra_kwargs = {
            'hash': {'read_only': True},
        }

    def create(self, validated_data):
        custom_hash = validated_data.pop('custom_hash', None)
        if custom_hash:
            validated_data['hash'] = custom_hash
        return UrlShort.objects.create(**validated_data,
                                       user_session_key=self.context['session_key'])

    def validate_custom_hash(self, value):
        custom_hash = value.replace(' ', '')
        if UrlShort.objects.filter(hash=custom_hash).exists():
            raise serializers.ValidationError('Hash exists')
        return custom_hash


class UrlShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShort
        fields = ('full_url', 'short_url', 'hash', 'created_at')
