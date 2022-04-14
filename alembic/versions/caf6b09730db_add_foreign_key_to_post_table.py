"""add foreign key to post table

Revision ID: caf6b09730db
Revises: 59d7334a4c3f
Create Date: 2022-04-14 15:58:37.256863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caf6b09730db'
down_revision = '59d7334a4c3f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column("posts","owner_id")
    pass
