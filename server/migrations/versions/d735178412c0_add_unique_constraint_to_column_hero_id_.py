"""add unique constraint to column hero_id and power_id

Revision ID: d735178412c0
Revises: da48c45b06b5
Create Date: 2024-10-13 14:25:40.321670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd735178412c0'
down_revision = 'da48c45b06b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes_powers', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_hero_id_power_id', ['hero_id', 'power_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes_powers', schema=None) as batch_op:
        batch_op.drop_constraint('uq_hero_id_power_id', type_='unique')

    # ### end Alembic commands ###
