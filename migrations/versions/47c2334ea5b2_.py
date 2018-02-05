"""Add bookmark meta field

Revision ID: 47c2334ea5b2
Revises: efd0d6a3c6d7
Create Date: 2018-02-03 16:58:40.876386

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '47c2334ea5b2'
down_revision = 'efd0d6a3c6d7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('bookmark', sa.Column('meta', postgresql.JSON(astext_type=sa.Text()), nullable=True))


def downgrade():
    op.drop_column('bookmark', 'meta')
