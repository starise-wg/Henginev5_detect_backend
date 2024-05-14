"""empty message

Revision ID: 64b277c5b357
Revises: 
Create Date: 2023-04-01 18:16:18.901210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64b277c5b357'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('captcha',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True, comment='验证邮箱'),
    sa.Column('captcha', sa.String(length=100), nullable=False, comment='验证码'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('is_used', sa.Boolean(), nullable=True, comment='是否使用'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dataset',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='数据集id'),
    sa.Column('dataset_name', sa.String(length=100), nullable=False, comment='数据集名称'),
    sa.Column('class_num', sa.Integer(), nullable=False, comment='类别数量'),
    sa.Column('total_num', sa.Integer(), nullable=False, comment='总数量'),
    sa.Column('train_num', sa.Integer(), nullable=False, comment='训练集数量'),
    sa.Column('val_num', sa.Integer(), nullable=False, comment='验证集数量'),
    sa.Column('test_exist', sa.Boolean(), nullable=False, comment='是否存在测试集'),
    sa.Column('test_num', sa.Integer(), nullable=True, comment='测试集数量'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='角色id'),
    sa.Column('role_name', sa.String(length=100), nullable=False, comment='角色名称'),
    sa.Column('role_desc', sa.String(length=100), nullable=False, comment='角色描述'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='图片id'),
    sa.Column('image_name', sa.String(length=100), nullable=False, comment='图片名称'),
    sa.Column('image_absolute_path', sa.Text(), nullable=True, comment='图片绝对路径'),
    sa.Column('image_relative_path', sa.Text(), nullable=True, comment='图片相对路径'),
    sa.Column('image_type', sa.String(length=100), nullable=False, comment='图片类型'),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['dataset.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('label',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='标注id'),
    sa.Column('label_name', sa.String(length=100), nullable=False, comment='标注名称'),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['dataset.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='用户id'),
    sa.Column('username', sa.String(length=100), nullable=False, comment='用户名'),
    sa.Column('password', sa.String(length=500), nullable=False, comment='密码'),
    sa.Column('email', sa.String(length=100), nullable=False, comment='邮箱'),
    sa.Column('join_time', sa.DateTime(), nullable=True, comment='加入时间'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='是否启用'),
    sa.Column('role_id', sa.Integer(), nullable=True, comment='用户角色'),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('weights',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='权重id'),
    sa.Column('weights_name', sa.String(length=100), nullable=False, comment='权重名称'),
    sa.Column('weights_relative_path', sa.Text(), nullable=False, comment='权重相对路径'),
    sa.Column('weights_absolute_path', sa.Text(), nullable=True, comment='权重绝对路径'),
    sa.Column('weights_version', sa.String(length=100), nullable=False, comment='权重版本'),
    sa.Column('enable', sa.Boolean(), nullable=False, comment='是否启用'),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['dataset.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detect_result',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='检测结果id'),
    sa.Column('detect_result', sa.Text(), nullable=False, comment='检测结果'),
    sa.Column('detect_result_image_name', sa.String(length=100), nullable=False, comment='检测结果图片名称'),
    sa.Column('detect_time', sa.DateTime(), nullable=True, comment='检测时间'),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_label_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='图片标注信息id'),
    sa.Column('image_id', sa.Integer(), nullable=True, comment='图片id'),
    sa.Column('label_id', sa.Integer(), nullable=True, comment='标注id'),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_label_info')
    op.drop_table('detect_result')
    op.drop_table('weights')
    op.drop_table('user')
    op.drop_table('label')
    op.drop_table('image')
    op.drop_table('role')
    op.drop_table('dataset')
    op.drop_table('captcha')
    # ### end Alembic commands ###
