"""Initial migration

Revision ID: ab306994677a
Revises: 4d861c61b131
Create Date: 2024-01-22 22:22:19.737488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab306994677a'
down_revision: Union[str, None] = '4d861c61b131'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('rating', sa.Integer(), nullable=True))
    op.drop_column('votes', 'value')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('value', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('votes', 'rating')
    # ### end Alembic commands ###
