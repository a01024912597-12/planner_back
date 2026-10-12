"""remove event title unique

Revision ID: 6ee4fd539aa2
Revises: 8764cc240a4d
Create Date: 2026-10-12 17:00:10.073225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ee4fd539aa2'
down_revision: Union[str, Sequence[str], None] = '8764cc240a4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "SYS_C008769",
        "events",
        type_="unique"
    )


def downgrade() -> None:
    op.create_unique_constraint(
        "SYS_C008769",
        "events",
        ["title"]
    )