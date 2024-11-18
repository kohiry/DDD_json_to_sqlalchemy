from datetime import date
from src.domain.common import BaseSchema


class BaseTariffSchema(BaseSchema):
    pass

class BaseCargoSchema(BaseSchema):
    pass

# class EnumCargo(Enum):
#     GLASS = 'Glass'
#     Other = 'Other'

class CargoSchema(BaseCargoSchema):
    cargo_type: str
    rate: str

class GetCalculateSchema(BaseSchema):
    date: date
    cargo_type: str
    cost: str


class GetTariffSchema(BaseTariffSchema):
    date: date


class TariffSchema(GetTariffSchema):
    cargos: list[CargoSchema]


class CreateTariffSchema(TariffSchema):
    pass




class UpdateTariffSchema(TariffSchema):
    pass


class DeleteTariffSchema(GetTariffSchema):
    pass


class CalculatedTariff(BaseTariffSchema):
    new_cost: float
