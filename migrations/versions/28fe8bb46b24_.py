"""empty message

Revision ID: 28fe8bb46b24
Revises: 7932e5760d00
Create Date: 2024-11-02 22:58:12.829735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28fe8bb46b24'
down_revision = '7932e5760d00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('completed_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
