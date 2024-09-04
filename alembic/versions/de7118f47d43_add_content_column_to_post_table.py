"""add content column to post table

Revision ID: de7118f47d43
Revises: 8621a6d49a3e
Create Date: 2024-09-03 21:04:36.371364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de7118f47d43'
down_revision: Union[str, None] = '8621a6d49a3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
