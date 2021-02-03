"""Initial_1

Revision ID: 0fdff0775c2a
Revises: 
Create Date: 2021-01-26 15:22:25.714973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fdff0775c2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False, comment='城市ID'),
    sa.Column('name', sa.String(length=80), nullable=False, comment='城市名稱'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False, comment='使用者ID'),
    sa.Column('city_id', sa.Integer(), nullable=True, comment='外鍵城市ID'),
    sa.Column('name', sa.String(length=80), nullable=False, comment='使用者名稱'),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False, comment='留言ID'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='外鍵使用者ID'),
    sa.Column('title', sa.String(length=120), nullable=False, comment='留言標題'),
    sa.Column('content', sa.String(length=120), nullable=False, comment='留言內容'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('user')
    op.drop_table('city')
    # ### end Alembic commands ###
