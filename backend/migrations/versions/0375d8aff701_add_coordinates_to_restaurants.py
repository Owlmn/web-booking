"""add_coordinates_to_restaurants

Revision ID: 0375d8aff701
Revises: 4364a8440007
Create Date: 2025-06-29 02:36:41.439963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0375d8aff701'
down_revision: Union[str, Sequence[str], None] = '4364a8440007'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurants', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('restaurants', sa.Column('longitude', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurants', 'longitude')
    op.drop_column('restaurants', 'latitude')
    # ### end Alembic commands ###
