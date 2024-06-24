"""init

Revision ID: 6c84ee3f4551
Revises: 
Create Date: 2024-04-20 20:07:59.242856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c84ee3f4551'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='homework'
    )
    op.create_table('products',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='homework'
    )
    op.create_table('product_cart_association',
    sa.Column('product_id', sa.Uuid(), nullable=False),
    sa.Column('cart_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['homework.carts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['homework.products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('product_id', 'cart_id'),
    schema='homework'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_cart_association', schema='homework')
    op.drop_table('products', schema='homework')
    op.drop_table('carts', schema='homework')
    # ### end Alembic commands ###