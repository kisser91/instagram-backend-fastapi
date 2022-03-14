"""add column content

Revision ID: 3a8b9e2abc91
Revises: 28300aab4cc9
Create Date: 2022-03-14 15:26:08.806108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a8b9e2abc91'
down_revision = '28300aab4cc9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts","content")
    pass
