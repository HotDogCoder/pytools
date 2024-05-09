from abc import ABC, abstractmethod
from apps.eeuu.domain.models.visa_model import VisaModel

class VisaRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def query(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def upload(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def post(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def get(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def put(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def delete(self, visa_model: VisaModel):
        return visa_model
