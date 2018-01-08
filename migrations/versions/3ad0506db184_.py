"""Enable hierarchical bookmarks

Revision ID: 3ad0506db184
Revises: 5ac0c69dd8bd
Create Date: 2018-01-09 01:18:10.535616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ad0506db184'
down_revision = '5ac0c69dd8bd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('bookmark', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'bookmark', 'bookmark', ['parent_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'bookmark', type_='foreignkey')
    op.drop_column('bookmark', 'parent_id')
