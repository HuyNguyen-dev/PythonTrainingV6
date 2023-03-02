"""set data to organization

Revision ID: e5ecb8ff5def
Revises: 196dfdc81687
Create Date: 2023-03-02 17:30:33.621902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String


# revision identifiers, used by Alembic.
revision = 'e5ecb8ff5def'
down_revision = '196dfdc81687'
branch_labels = None
depends_on = None


def upgrade() -> None:
    organization_table = table('organization',
        column('username', String)
    )
    op.bulk_insert(organization_table,
    [
        {'username':'TMA'},
        {'username':'TMA-BD'},
        {'username':'TMA-US'},
    ],
    multiinsert=False
)


def downgrade() -> None:
    pass
