from src.domain.schema import CreateTariffSchema
from src.domain.schema import CargoSchema


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
