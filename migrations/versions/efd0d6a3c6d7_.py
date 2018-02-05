"""Add google_id

Revision ID: efd0d6a3c6d7
Revises: 3ad0506db184
Create Date: 2018-01-29 12:33:31.975051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd0d6a3c6d7'
down_revision = '3ad0506db184'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('google_id', sa.String(length=255), nullable=True))
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.create_unique_constraint('unique_google_id', 'user', ['google_id'])


def downgrade():
    op.drop_constraint('unique_google_id', 'user', type_='unique')
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('user', 'google_id')
