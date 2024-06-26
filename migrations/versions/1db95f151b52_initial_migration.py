"""Initial migration

Revision ID: 1db95f151b52
Revises: 
Create Date: 2024-05-02 05:38:27.659362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1db95f151b52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('attendence', schema=None) as batch_op:
        batch_op.alter_column('rollno',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('attendance',
               existing_type=mysql.INTEGER(display_width=100),
               nullable=True)

    with op.batch_alter_table('department', schema=None) as batch_op:
        batch_op.alter_column('branch',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               nullable=True)

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('rollno',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=50),
               nullable=True)
        batch_op.alter_column('sname',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('sem',
               existing_type=mysql.INTEGER(display_width=20),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('branch',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('number',
               existing_type=mysql.VARCHAR(length=12),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=100),
               nullable=True)

    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=52),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               nullable=True)

    with op.batch_alter_table('trig', schema=None) as batch_op:
        batch_op.alter_column('rollno',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('action',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('timestamp',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=100),
               nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=500),
               type_=sa.String(length=1000),
               nullable=True)
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)

    with op.batch_alter_table('trig', schema=None) as batch_op:
        batch_op.alter_column('timestamp',
               existing_type=sa.String(length=100),
               type_=mysql.DATETIME(),
               nullable=False)
        batch_op.alter_column('action',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('rollno',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               nullable=False)

    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=52),
               nullable=False)

    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.String(length=100),
               type_=mysql.TEXT(),
               nullable=False)
        batch_op.alter_column('number',
               existing_type=mysql.VARCHAR(length=12),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('branch',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('sem',
               existing_type=mysql.INTEGER(display_width=20),
               nullable=False)
        batch_op.alter_column('sname',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('rollno',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=20),
               nullable=False)

    with op.batch_alter_table('department', schema=None) as batch_op:
        batch_op.alter_column('branch',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               nullable=False)

    with op.batch_alter_table('attendence', schema=None) as batch_op:
        batch_op.alter_column('attendance',
               existing_type=mysql.INTEGER(display_width=100),
               nullable=False)
        batch_op.alter_column('rollno',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=20),
               nullable=False)

    op.drop_table('contact')
    # ### end Alembic commands ###
