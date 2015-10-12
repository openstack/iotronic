#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""initial migration

Revision ID: 2581ebaf0cb2
Revises: None
Create Date: 2014-01-17 12:14:07.754448

"""

# revision identifiers, used by Alembic.
revision = '2581ebaf0cb2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # commands auto generated by Alembic - please adjust!
    op.create_table(
        'conductors',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('hostname', sa.String(length=255), nullable=False),
        sa.Column('drivers', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('hostname', name='uniq_conductors0hostname'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'chassis',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('extra', sa.Text(), nullable=True),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid', name='uniq_chassis0uuid'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_table(
        'nodes',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('instance_uuid', sa.String(length=36), nullable=True),
        sa.Column('chassis_id', sa.Integer(), nullable=True),
        sa.Column('power_state', sa.String(length=15), nullable=True),
        sa.Column('target_power_state', sa.String(length=15), nullable=True),
        sa.Column('provision_state', sa.String(length=15), nullable=True),
        sa.Column('target_provision_state', sa.String(length=15),
                  nullable=True),
        sa.Column('last_error', sa.Text(), nullable=True),
        sa.Column('properties', sa.Text(), nullable=True),
        sa.Column('driver', sa.String(length=15), nullable=True),
        sa.Column('driver_info', sa.Text(), nullable=True),
        sa.Column('reservation', sa.String(length=255), nullable=True),
        sa.Column('maintenance', sa.Boolean(), nullable=True),
        sa.Column('extra', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['chassis_id'], ['chassis.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid', name='uniq_nodes0uuid'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    op.create_index('node_instance_uuid', 'nodes', ['instance_uuid'],
                    unique=False)
    op.create_table(
        'ports',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('address', sa.String(length=18), nullable=True),
        sa.Column('node_id', sa.Integer(), nullable=True),
        sa.Column('extra', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('address', name='uniq_ports0address'),
        sa.UniqueConstraint('uuid', name='uniq_ports0uuid'),
        mysql_ENGINE='InnoDB',
        mysql_DEFAULT_CHARSET='UTF8'
    )
    # end Alembic commands


def downgrade():
    raise NotImplementedError(('Downgrade from initial migration is'
                              ' unsupported.'))
