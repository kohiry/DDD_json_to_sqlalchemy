"""add tariff and cargo tables

Revision ID: 637f316dc156
Revises: 
Create Date: 2024-11-18 10:16:18.151725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '637f316dc156'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tariff_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date')
    )
    op.create_table('cargo_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cargo_type', sa.String(), nullable=False),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.Column('tariff_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tariff_id'], ['tariff_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cargo_table')
    op.drop_table('tariff_table')
    # ### end Alembic commands ###
