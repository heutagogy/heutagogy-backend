"""Add tags for bookmarks

Revision ID: b07014167199
Revises: 9593b881ca57
Create Date: 2017-12-20 00:32:19.491903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b07014167199'
down_revision = '9593b881ca57'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('bookmark', sa.Column('tags', postgresql.ARRAY(sa.Text()), nullable=True))


def downgrade():
    op.drop_column('bookmark', 'tags')
