"""add_is_enabled_flag

Revision ID: cbf3aa0119c2
Revises: 3284c714b7fd
Create Date: 2023-12-12 19:47:53.121693

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'cbf3aa0119c2'
down_revision: Union[str, None] = '3284c714b7fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site', sa.Column('is_enabled', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site', 'is_enabled')
    # ### end Alembic commands ###