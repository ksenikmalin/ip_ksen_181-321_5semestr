from import_export import resources
from repairs.models import Services


class ServicesResources(resources.ModelResource):
    class Meta:
        model = Services
