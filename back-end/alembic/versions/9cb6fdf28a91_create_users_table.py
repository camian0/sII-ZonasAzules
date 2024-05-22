"""create users table

Revision ID: 9cb6fdf28a91
Revises: 
Create Date: 2024-05-15 13:57:11.826727

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9cb6fdf28a91"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
        ),
        sa.Column("username", sa.String(50), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("password", sa.String(50), nullable=False),
        sa.Column("role", sa.String(50), nullable=False),
        sa.Column("telefono", sa.String(50)),
    )


def downgrade() -> None:
    op.drop_table("users")
