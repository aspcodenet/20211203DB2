"""AddedPostal code

Revision ID: 844d409732e2
Revises: 13c11f5b32d7
Create Date: 2021-12-03 09:34:01.717715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844d409732e2'
down_revision = '13c11f5b32d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('postalcode', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'postalcode')
    # ### end Alembic commands ###
