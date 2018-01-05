"""Add notes

Revision ID: 5ac0c69dd8bd
Revises: b07014167199
Create Date: 2018-01-05 20:35:28.011011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ac0c69dd8bd'
down_revision = 'b07014167199'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bookmark_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['bookmark_id'], ['bookmark.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('note')
