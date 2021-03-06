"""update_message_table

Revision ID: cc29e01f1132
Revises: 0fdff0775c2a
Create Date: 2021-01-27 19:07:40.930446

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cc29e01f1132'
down_revision = '0fdff0775c2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('city', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment=None,
               existing_comment='城市ID',
               autoincrement=True)
    op.alter_column('city', 'name',
               existing_type=mysql.VARCHAR(length=80),
               comment=None,
               existing_comment='城市名稱',
               existing_nullable=False)
    op.alter_column('message', 'content',
               existing_type=mysql.VARCHAR(length=120),
               comment=None,
               existing_comment='留言內容',
               existing_nullable=False)
    op.alter_column('message', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment=None,
               existing_comment='留言ID',
               autoincrement=True)
    op.alter_column('message', 'title',
               existing_type=mysql.VARCHAR(length=120),
               comment=None,
               existing_comment='留言標題',
               existing_nullable=False)
    op.alter_column('message', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               comment=None,
               existing_comment='外鍵使用者ID',
               existing_nullable=True)
    op.drop_index('content', table_name='message')
    op.drop_index('title', table_name='message')
    op.alter_column('user', 'city_id',
               existing_type=mysql.INTEGER(display_width=11),
               comment=None,
               existing_comment='外鍵城市ID',
               existing_nullable=True)
    op.alter_column('user', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment=None,
               existing_comment='使用者ID',
               autoincrement=True)
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=80),
               comment=None,
               existing_comment='使用者名稱',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=80),
               comment='使用者名稱',
               existing_nullable=False)
    op.alter_column('user', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='使用者ID',
               autoincrement=True)
    op.alter_column('user', 'city_id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='外鍵城市ID',
               existing_nullable=True)
    op.create_index('title', 'message', ['title'], unique=True)
    op.create_index('content', 'message', ['content'], unique=True)
    op.alter_column('message', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='外鍵使用者ID',
               existing_nullable=True)
    op.alter_column('message', 'title',
               existing_type=mysql.VARCHAR(length=120),
               comment='留言標題',
               existing_nullable=False)
    op.alter_column('message', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='留言ID',
               autoincrement=True)
    op.alter_column('message', 'content',
               existing_type=mysql.VARCHAR(length=120),
               comment='留言內容',
               existing_nullable=False)
    op.alter_column('city', 'name',
               existing_type=mysql.VARCHAR(length=80),
               comment='城市名稱',
               existing_nullable=False)
    op.alter_column('city', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='城市ID',
               autoincrement=True)
    # ### end Alembic commands ###
