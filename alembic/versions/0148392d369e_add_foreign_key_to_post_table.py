"""add foreign-key to post table

Revision ID: 0148392d369e
Revises: d255f0a97c29
Create Date: 2022-03-14 16:34:52.278295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0148392d369e'
down_revision = 'd255f0a97c29'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts",referent_table="users", local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
