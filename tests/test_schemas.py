
from agentic_cad.schemas import CADPlan, HoleSpec

def test_plate_plan():
    plan = CADPlan(
        part_name="four_hole_plate",
        operation="plate",
        dimensions={
            "length": 80,
            "width": 40,
            "thickness": 10
        },
        holes=[
            HoleSpec(
                diameter=4,
                positions=[
                    (-20, -10),
                    (20, -10),
                    (-20, 10),
                    (20, 10)
                ],
                depth="through"
            )
        ]
    )

    assert plan.dimensions["length"] == 80
    assert len(plan.holes[0].positions) == 4
