"""empty message

Revision ID: 2f8813af460d
Revises: 
Create Date: 2017-01-22 22:45:26.855474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f8813af460d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('bookmark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('read', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('first_name', sa.String(length=255), server_default='', nullable=False),
    sa.Column('last_name', sa.String(length=255), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('user')
    op.drop_table('bookmark')
