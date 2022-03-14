"""user table

Revision ID: d255f0a97c29
Revises: 3a8b9e2abc91
Create Date: 2022-03-14 15:54:40.653292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd255f0a97c29'
down_revision = '3a8b9e2abc91'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_ad", sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
