"""empty message

Revision ID: 35cb9124ed71
Revises: 
Create Date: 2022-03-05 17:52:26.588298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35cb9124ed71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('lastname', sa.String(length=250), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('specie', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('specie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=False),
    sa.Column('lenguage', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('manufacturer', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favoritcharacter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('characters_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['characters_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritplanet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritspecie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('specie_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['specie_id'], ['specie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritstarship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starship_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['starship_id'], ['starship.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritstarship')
    op.drop_table('favoritspecie')
    op.drop_table('favoritplanet')
    op.drop_table('favoritcharacter')
    op.drop_table('users')
    op.drop_table('starship')
    op.drop_table('specie')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###