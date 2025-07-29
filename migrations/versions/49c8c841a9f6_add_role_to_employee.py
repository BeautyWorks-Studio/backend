"""Add role to employee

Revision ID: 49c8c841a9f6
Revises: a17dd99e0bb1
Create Date: 2025-07-29 09:50:28.873600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c8c841a9f6'
down_revision = 'a17dd99e0bb1'
branch_labels = None
depends_on = None


from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '49c8c841a9f6'
down_revision = 'a17dd99e0bb1'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('employees') as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=True))
        batch_op.create_unique_constraint('uq_employee_email', ['email'])

def downgrade():
    with op.batch_alter_table('employees') as batch_op:
        batch_op.drop_constraint('uq_employee_email', type_='unique')
        batch_op.drop_column('role')
