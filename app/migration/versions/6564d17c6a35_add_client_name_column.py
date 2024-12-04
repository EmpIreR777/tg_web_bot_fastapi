"""add client_name column

Revision ID: 6564d17c6a35
Revises: 8ffe2b521738
Create Date: 2024-10-05 15:12:45.951582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6564d17c6a35'
down_revision: Union[str, None] = '8ffe2b521738'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('client_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('applications', 'client_name')
    # ### end Alembic commands ###
