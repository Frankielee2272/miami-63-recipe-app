"""empty message

Revision ID: 7696ba66d8ad
Revises: 4c5eb1ca173f
Create Date: 2024-06-11 21:40:37.629967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7696ba66d8ad'
down_revision = '4c5eb1ca173f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recipe_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('ingredients', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('directions', sa.String(), nullable=False))
        batch_op.drop_column('recipe_ingredients')
        batch_op.drop_column('recipe_directions')
        batch_op.drop_column('recipe_title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recipe_title', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('recipe_directions', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('recipe_ingredients', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('directions')
        batch_op.drop_column('ingredients')
        batch_op.drop_column('recipe_name')

    # ### end Alembic commands ###
