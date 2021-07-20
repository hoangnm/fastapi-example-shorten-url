"""set unique for generated url

Revision ID: 8463cf216476
Revises: d65674e7612d
Create Date: 2021-07-20 11:34:37.903294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8463cf216476'
down_revision = 'd65674e7612d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''DELETE FROM "shorten_url" WHERE generated_url = '5da8c330b9511dee39c6976dfe634cea'; ''')
    op.create_unique_constraint('uq_generated_url', 'shorten_url', ['generated_url'])


def downgrade():
    op.drop_constraint('uq_generated_url', 'shorten_url')

