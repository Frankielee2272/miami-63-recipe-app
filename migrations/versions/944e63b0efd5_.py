"""empty message

Revision ID: 944e63b0efd5
Revises: e2e187a352e2
Create Date: 2024-05-30 00:04:12.657191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '944e63b0efd5'
down_revision = 'e2e187a352e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
