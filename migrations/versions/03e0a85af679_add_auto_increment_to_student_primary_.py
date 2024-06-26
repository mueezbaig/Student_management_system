"""Add auto-increment to Student primary key

Revision ID: 03e0a85af679
Revises: 1db95f151b52
Create Date: 2024-05-02 12:43:19.532931

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '03e0a85af679'
down_revision = '1db95f151b52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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

    # ### end Alembic commands ###
