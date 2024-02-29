# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Tests for the microgrid component wrapper."""

import pytest

# pylint: disable=no-name-in-module
from frequenz.api.common.components_pb2 import ComponentCategory

# pylint: enable=no-name-in-module
import frequenz.client.microgrid._component as cp


def test_component_category_from_protobuf() -> None:
    """Test the creating component category from protobuf."""
    assert (
        cp.component_category_from_protobuf(
            ComponentCategory.COMPONENT_CATEGORY_UNSPECIFIED
        )
        == cp.ComponentCategory.NONE
    )

    assert (
        cp.component_category_from_protobuf(ComponentCategory.COMPONENT_CATEGORY_GRID)
        == cp.ComponentCategory.GRID
    )

    assert (
        cp.component_category_from_protobuf(ComponentCategory.COMPONENT_CATEGORY_METER)
        == cp.ComponentCategory.METER
    )

    assert (
        cp.component_category_from_protobuf(
            ComponentCategory.COMPONENT_CATEGORY_INVERTER
        )
        == cp.ComponentCategory.INVERTER
    )

    assert (
        cp.component_category_from_protobuf(
            ComponentCategory.COMPONENT_CATEGORY_BATTERY
        )
        == cp.ComponentCategory.BATTERY
    )

    assert (
        cp.component_category_from_protobuf(
            ComponentCategory.COMPONENT_CATEGORY_EV_CHARGER
        )
        == cp.ComponentCategory.EV_CHARGER
    )

    assert cp.component_category_from_protobuf(666) == cp.ComponentCategory.NONE  # type: ignore

    with pytest.raises(ValueError):
        cp.component_category_from_protobuf(ComponentCategory.COMPONENT_CATEGORY_SENSOR)


# pylint: disable=invalid-name
def test_Component() -> None:
    """Test the component category."""
    c0 = cp.Component(0, cp.ComponentCategory.GRID)
    assert c0.is_valid()

    c1 = cp.Component(1, cp.ComponentCategory.GRID)
    assert c1.is_valid()

    c4 = cp.Component(4, cp.ComponentCategory.METER)
    assert c4.is_valid()

    c5 = cp.Component(5, cp.ComponentCategory.INVERTER)
    assert c5.is_valid()

    c6 = cp.Component(6, cp.ComponentCategory.BATTERY)
    assert c6.is_valid()

    c7 = cp.Component(7, cp.ComponentCategory.EV_CHARGER)
    assert c7.is_valid()

    invalid_grid_id = cp.Component(-1, cp.ComponentCategory.GRID)
    assert not invalid_grid_id.is_valid()

    invalid_type = cp.Component(666, -1)  # type: ignore
    assert not invalid_type.is_valid()

    another_invalid_type = cp.Component(666, 666)  # type: ignore
    assert not another_invalid_type.is_valid()
