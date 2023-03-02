"""update data in user_table

Revision ID: 8c6fd5972b10
Revises: 444269246297
Create Date: 2023-03-02 18:11:24.750929

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String,Integer

# revision identifiers, used by Alembic.
revision = '8c6fd5972b10'
down_revision = '444269246297'
branch_labels = None
depends_on = None


def upgrade() -> None:
    user = table('user',
        column('org_id', Integer)
    )
    op.execute(
        user.update().values({'org_id':op.inline_literal(1)})
    )


def downgrade() -> None:
    pass
