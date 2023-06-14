"""Fix bag in Document table

Revision ID: 9222ee124d18
Revises: 2a6d211f9d6b
Create Date: 2023-06-13 17:28:14.844401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9222ee124d18'
down_revision = '2a6d211f9d6b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('count', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'documents', ['user_id'])
    op.drop_column('documents', 'document_count')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('document_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'documents', type_='unique')
    op.drop_column('documents', 'count')
    # ### end Alembic commands ###