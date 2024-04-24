"""init

Revision ID: 466e400da3f7
Revises: 
Create Date: 2024-04-24 00:05:13.624350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '466e400da3f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('province', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('major', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###