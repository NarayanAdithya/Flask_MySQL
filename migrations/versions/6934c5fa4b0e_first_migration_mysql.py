"""First Migration MYSQL

Revision ID: 6934c5fa4b0e
Revises: 
Create Date: 2021-06-29 23:16:53.023002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6934c5fa4b0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('user_role', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(length=64), nullable=True),
    sa.Column('course_code', sa.String(length=64), nullable=True),
    sa.Column('course_description', sa.String(length=120), nullable=True),
    sa.Column('course_by_faculty', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_by_faculty'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_courses_course_code'), 'courses', ['course_code'], unique=False)
    op.create_index(op.f('ix_courses_course_name'), 'courses', ['course_name'], unique=True)
    op.create_table('association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('courses_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['courses_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_index(op.f('ix_association_courses_id'), 'association', ['courses_id'], unique=False)
    op.create_index(op.f('ix_association_user_id'), 'association', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_association_user_id'), table_name='association')
    op.drop_index(op.f('ix_association_courses_id'), table_name='association')
    op.drop_table('association')
    op.drop_index(op.f('ix_courses_course_name'), table_name='courses')
    op.drop_index(op.f('ix_courses_course_code'), table_name='courses')
    op.drop_table('courses')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###