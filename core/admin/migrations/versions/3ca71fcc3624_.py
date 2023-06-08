"""Add Token.rights

Revision ID: 3ca71fcc3624
Revises: 6b8f5e8caaa9
Create Date: 2023-06-08 16:19:15.605547

"""

# revision identifiers, used by Alembic.
revision = '3ca71fcc3624'
down_revision = '6b8f5e8caaa9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('token', sa.Column('rights', sa.Enum('full', 'send_only', 'receive_only', name='rights'), nullable=True))


def downgrade():
    op.drop_column('token', 'rights')