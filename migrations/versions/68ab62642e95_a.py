"""a

Revision ID: 68ab62642e95
Revises: 
Create Date: 2023-02-12 12:06:34.463988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68ab62642e95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('block', schema=None) as batch_op:
        batch_op.add_column(sa.Column('proof', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('prev_hash', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('timestamp', sa.String(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('block', schema=None) as batch_op:
        batch_op.drop_column('timestamp')
        batch_op.drop_column('prev_hash')
        batch_op.drop_column('proof')

    # ### end Alembic commands ###