"""bookmark.user: string -> integer

Revision ID: 797321279ea1
Revises: 2f8813af460d
Create Date: 2017-01-23 01:23:04.078995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '797321279ea1'
down_revision = '2f8813af460d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('bookmark', 'user', type_=sa.Integer(), existing_nullable=False,
            postgresql_using='bookmark.user::integer')
    op.create_foreign_key('bookmark_user_fkey', 'bookmark', 'user', ['user'], ['id'])


def downgrade():
    op.drop_constraint('bookmark_user_fkey', 'bookmark', type_='foreignkey')
    op.alter_column('bookmark', 'user', type_=sa.String(), existing_nullable=False)
