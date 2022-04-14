"""add content column to post table

Revision ID: e7d1986ced36
Revises: 6584894e07ac
Create Date: 2022-04-14 15:38:33.009285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7d1986ced36'
down_revision = '6584894e07ac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
