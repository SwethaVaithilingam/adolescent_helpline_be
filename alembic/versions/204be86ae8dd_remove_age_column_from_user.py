"""remove age column from user

Revision ID: 204be86ae8dd
Revises: 784932b0dddb
Create Date: 2026-02-19 12:10:43.826362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '204be86ae8dd'
down_revision: Union[str, Sequence[str], None] = '784932b0dddb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('users', 'age')


def downgrade():
    op.add_column('users',
        sa.Column('age', sa.Integer(), nullable=True)
    )
