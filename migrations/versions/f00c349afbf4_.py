"""empty message

Revision ID: f00c349afbf4
Revises: a40e44cb3712
Create Date: 2020-11-03 13:22:25.954341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00c349afbf4'
down_revision = 'a40e44cb3712'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('password', sa.String(length=128), nullable=True))
    op.drop_column('teacher', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('teacher', 'password')
    # ### end Alembic commands ###