"""empty message

Revision ID: aa52d1423b94
Revises:
Create Date: 2023-03-07 02:05:35.524193

"""
import sqlalchemy as sa
from alembic import op

from api.v1.car.enums import CarColorsEnum
from api.v1.car.enums import CarTypeEnum
from api.v1.car.model import CarColor
from api.v1.car.model import CarType

# revision identifiers, used by Alembic.
revision = "aa52d1423b94"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "car_color",
        sa.Column(
            "color_name",
            sa.Enum("YELLOW", "BLUE", "GRAY", name="carcolorsenum"),
            nullable=False,
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "car_type",
        sa.Column(
            "type_car_name",
            sa.Enum("HATCH", "SEDAN", "CONVERTIBLE", name="cartypeenum"),
            nullable=False,
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "person",
        sa.Column("name", sa.String(length=155), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "car",
        sa.Column("car_name", sa.String(length=155), nullable=False),
        sa.Column("color_id", sa.UUID(), nullable=False),
        sa.Column("type_car_id", sa.UUID(), nullable=False),
        sa.Column("person_id", sa.UUID(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["color_id"],
            ["car_color.id"],
        ),
        sa.ForeignKeyConstraint(["person_id"], ["person.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["type_car_id"],
            ["car_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("car_name"),
    )
    # ### end Alembic commands ###
    for value in CarTypeEnum:
        op.execute(sa.insert(CarType).values(type_car_name=value.name))

    for value in CarColorsEnum:
        op.execute(sa.insert(CarColor).values(color_name=value.name))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("car")
    op.drop_table("person")
    op.drop_table("car_type")
    op.drop_table("car_color")
    # ### end Alembic commands ###
