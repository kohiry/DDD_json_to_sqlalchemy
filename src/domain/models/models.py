from sqlalchemy import Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.infrastructure.database.base import Base


class TariffModel(Base):
    __tablename__ = "tariff_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[Date] = mapped_column(Date, nullable=False, unique=True)

    # Связь с CargoModel (один тариф может иметь несколько грузов)
    cargos: Mapped[list["CargoModel"]] = relationship(
        "CargoModel", back_populates="tariff", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<TariffModel(id={self.id}, date={self.date})>"


class CargoModel(Base):
    __tablename__ = "cargo_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cargo_type: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[str] = mapped_column(String, nullable=False)

    # Внешний ключ к TariffModel
    tariff_id: Mapped[int] = mapped_column(Integer, ForeignKey("tariff_table.id", ondelete="CASCADE"))

    # Связь с TariffModel (многие грузы относятся к одному тарифу)
    tariff: Mapped[TariffModel] = relationship("TariffModel", back_populates="cargos")

    def __repr__(self):
        return f"<CargoModel(id={self.id}, cargo_type='{self.cargo_type}', rate={self.rate})>"
