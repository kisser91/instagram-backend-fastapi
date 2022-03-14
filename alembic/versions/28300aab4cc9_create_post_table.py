"""create post table

Revision ID: 28300aab4cc9
Revises: 
Create Date: 2022-03-14 01:27:29.028132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28300aab4cc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
