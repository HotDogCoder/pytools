from apps.eeuu.application.repositories_interfaces.visa_repository_interface import VisaRepositoryInterface
from apps.eeuu.domain.models.visa_model import VisaModel

class VisaRepository(VisaRepositoryInterface):
    def __init__(self):
        super().__init__()

    def query(self, visa_model: VisaModel):
        return visa_model
    def upload(self, visa_model: VisaModel):
        return visa_model
    def post(self, visa_model: VisaModel):
        return visa_model
    def get(self, visa_model: VisaModel):
        return visa_model
    def put(self, visa_model: VisaModel):
        return visa_model
    def delete(self, visa_model: VisaModel):
        return visa_model
