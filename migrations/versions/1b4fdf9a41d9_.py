"""empty message

Revision ID: 1b4fdf9a41d9
Revises: b07014167199
Create Date: 2018-01-03 23:48:19.625104

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1b4fdf9a41d9'
down_revision = 'b07014167199'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.create_table('bookmark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('read', sa.DateTime(), nullable=True),
    sa.Column('tags', postgresql.ARRAY(sa.Text()), nullable=True),
    sa.Column('content_html', sa.Text(), nullable=True),
    sa.Column('content_text', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookmark')
    op.drop_table('user')
    # ### end Alembic commands ###
