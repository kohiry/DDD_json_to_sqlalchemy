from datetime import date
from src.domain.common import BaseSchema


__all__ = [
    "TariffSchema",
]


class BaseTariffSchema(BaseSchema):
    pass

class BaseCargoSchema(BaseSchema):
    pass

# class EnumCargo(Enum):
#     GLASS = 'Glass'
#     Other = 'Other'

class CargoSchema(BaseCargoSchema):
    cargo_type: str
    rate: float


class TariffSchema(BaseTariffSchema):
    date: date
    cargos: list[CargoSchema]


class CreateTariffSchema(TariffSchema):
    pass

class GetTariffSchema(BaseTariffSchema):
    date: date


class UpdateTariffSchema(TariffSchema):
    pass


class DeleteTariffSchema(GetTariffSchema):
    pass


class CalculateTariff(BaseTariffSchema):
    date: date
    cost: float
