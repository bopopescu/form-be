"""empty message

Revision ID: fdba6beeee31
Revises: 43837d67d975
Create Date: 2019-07-19 14:38:14.884809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdba6beeee31'
down_revision = '43837d67d975'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=191), nullable=False),
    sa.Column('username', sa.String(length=191), nullable=False),
    sa.Column('fullname', sa.String(length=191), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('id_token', sa.String(length=512), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('role', sa.Enum('admin', 'moderator', 'viewer', name='role'), nullable=True),
    sa.Column('last_login', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
