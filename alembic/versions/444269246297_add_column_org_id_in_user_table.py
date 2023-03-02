"""add column org_id in user_table

Revision ID: 444269246297
Revises: e5ecb8ff5def
Create Date: 2023-03-02 17:48:19.220302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '444269246297'
down_revision = 'e5ecb8ff5def'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.create_foreign_key(
    #         "org_id_foreign_key", "organization",
    #         "user", ["id"], ["org_id"])
    
    op.add_column('user', sa.Column('org_id', sa.Integer(),sa.ForeignKey('organization.id')))


def downgrade() -> None:
    pass
