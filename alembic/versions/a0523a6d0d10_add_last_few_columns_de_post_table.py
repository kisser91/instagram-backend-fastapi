"""add last few columns de post table

Revision ID: a0523a6d0d10
Revises: 0148392d369e
Create Date: 2022-03-14 17:05:09.647572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0523a6d0d10'
down_revision = '0148392d369e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        'published', sa.Boolean(), nullable=True, server_default="TRUE"),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'
        )),)
    pass

def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts', "created_ad")
    pass
