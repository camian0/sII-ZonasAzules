"""add unique email constraint

Revision ID: c05a7c617250
Revises: 9cb6fdf28a91
Create Date: 2024-05-21 20:14:08.543923

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c05a7c617250"
down_revision: Union[str, None] = "9cb6fdf28a91"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint("unique_email", "users", ["email"])


def downgrade() -> None:
    op.drop_constraint("unique_email", "users", "unique")
