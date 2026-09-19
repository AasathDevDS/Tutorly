from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields = ['id']

    def _validate_sri_lankan_phone(self, value, field_name):
        if value is not None and value != "":
            # Integer-ah vandhaalum string-ah convert pannidum
            value_str = str(value).strip()
            if len(value_str) == 9 and value_str.startswith('7'):
                value_str = '0' + value_str

            if not value_str.isdigit():
                raise serializers.ValidationError(f"{field_name} must contain only digits.")
            if len(value_str) != 10:
                raise serializers.ValidationError(f"{field_name} must be exactly 10 digits (e.g., 0771234567).")
            
            return value_str
        return value

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required.")
        return self._validate_sri_lankan_phone(value, "Phone Number")

    def validate_whatsapp_number(self, value):
        # Null or empty string aana skip pannidum, value irundha validate aagum
        if not value:
            return value 
        return self._validate_sri_lankan_phone(value, "WhatsApp Number")