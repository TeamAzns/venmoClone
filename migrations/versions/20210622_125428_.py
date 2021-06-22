"""empty message

Revision ID: 9b6a41b11498
Revises: 
Create Date: 2021-06-22 12:54:28.682846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b6a41b11498'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('hashed_password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('phonenumber', sa.String(length=11), nullable=True),
    sa.Column('profileImage', sa.String(length=256), nullable=True),
    sa.Column('balance', sa.Float(precision=10, decimal_return_scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('friends',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('requester', sa.Integer(), nullable=False),
    sa.Column('accepter', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['accepter'], ['users.id'], ),
    sa.ForeignKeyConstraint(['requester'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paymentdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('debit_card', sa.Integer(), nullable=True),
    sa.Column('bank', sa.String(length=50), nullable=True),
    sa.Column('billing_address', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Float(precision=10, asdecimal=True, decimal_return_scale=2), nullable=False),
    sa.Column('request', sa.Boolean(), nullable=True),
    sa.Column('sender', sa.Integer(), nullable=False),
    sa.Column('receiver', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('transactions_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transactions_id'], ['transactions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('transactions')
    op.drop_table('paymentdetails')
    op.drop_table('friends')
    op.drop_table('users')
    # ### end Alembic commands ###
