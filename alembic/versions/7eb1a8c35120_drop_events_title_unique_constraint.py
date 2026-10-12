"""drop events title unique constraint

Revision ID: 7eb1a8c35120
Revises: 6ee4fd539aa2
Create Date: 2026-10-12 17:01:38.495101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7eb1a8c35120'
down_revision: Union[str, Sequence[str], None] = '6ee4fd539aa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
