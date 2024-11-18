from decimal import Decimal, InvalidOperation

from src.core import get_logger
from src.domain.schema import CreateTariffSchema
from src.domain.schema import CargoSchema

logger = get_logger()


def cast_from_json_to_schema(data):
    schemas: list[CreateTariffSchema] = []
    for date in data:
        schemas.append(
            CreateTariffSchema(
                date=date,
                cargos=[
                    CargoSchema.model_validate(value)
                    for value in data[date]
                ]
            )
        )
    return schemas


def new_cost(value1: str, value2: str) -> str:
    try:
        num1 = Decimal(value1)
        num2 = Decimal(value2)

        result = num1 * num2

        return str(result)
    except (InvalidOperation, ValueError):
        raise ValueError("Invalid input: both inputs must be valid decimal numbers.")
