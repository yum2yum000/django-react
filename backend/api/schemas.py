from rest_framework.schemas.openapi import SchemaGenerator


class CustomSchema(SchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema["info"]["termsOfSecvice"] = 'https://test.com'
        return schema
