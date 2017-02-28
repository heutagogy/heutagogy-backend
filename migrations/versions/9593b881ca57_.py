"""empty message

Revision ID: 9593b881ca57
Revises: 797321279ea1
Create Date: 2017-02-28 23:45:23.295794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9593b881ca57'
down_revision = '797321279ea1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('bookmark', sa.Column('content_html', sa.Text(), nullable=True))
    op.add_column('bookmark', sa.Column('content_text', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('bookmark', 'content_text')
    op.drop_column('bookmark', 'content_html')
