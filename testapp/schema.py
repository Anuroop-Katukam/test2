import coreapi
from rest_framework.schemas import AutoSchema



class fileSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method in ['POST', 'PUT']:
            extra_fields = [
                            coreapi.Field('field_name'),
                                ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields
