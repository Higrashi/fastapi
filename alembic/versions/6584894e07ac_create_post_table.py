"""create post table

Revision ID: 6584894e07ac
Revises: 
Create Date: 2022-04-14 15:17:59.252700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6584894e07ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String,nullable=False)
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
