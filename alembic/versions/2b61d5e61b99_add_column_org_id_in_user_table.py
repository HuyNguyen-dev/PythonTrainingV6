"""add column org_id in user_table

Revision ID: 2b61d5e61b99
Revises: 585f03c0fb31
Create Date: 2023-03-02 17:11:52.630568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b61d5e61b99'
down_revision = '585f03c0fb31'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user', sa.Column('org_id', sa.Integer(),sa.ForeignKey('organization.id')))


def downgrade() -> None:
    pass
