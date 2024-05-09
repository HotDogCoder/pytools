import json
from apps.eeuu.application.services.visa_service import VisaService
from apps.eeuu.domain.models.visa_model import VisaModel

class VisaController:
    def __init__(self):
        super().__init__()
        self.visa_service = VisaService()

    def query(self, visa_model: VisaModel):
        return self.visa_service.query(visa_model)
    def upload(self, visa_model: VisaModel):
        return self.visa_service.upload(visa_model)
    def post(self, visa_model: VisaModel):
        return self.visa_service.post(visa_model)
    def get(self, visa_model: VisaModel):
        print('VisaController.get')
        print(visa_model.email)
        print(visa_model.password)
        print(visa_model.is_schedule)
        print(visa_model.intent_limit_input)
        while visa_model.result == False:
            self.visa_service.get(visa_model)
        return visa_model
    def put(self, visa_model: VisaModel):
        return self.visa_service.put(visa_model)
    def delete(self, visa_model: VisaModel):
        return self.visa_service.delete(visa_model)
