"""drop events title unique

Revision ID: 18ebf7aec2f1
Revises: 7eb1a8c35120
Create Date: 2026-10-12 17:03:10.856369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18ebf7aec2f1'
down_revision: Union[str, Sequence[str], None] = '7eb1a8c35120'
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