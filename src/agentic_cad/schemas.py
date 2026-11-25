from typing import Literal
from pydantic import BaseModel, Field

class HoleSpec(BaseModel):
    diameter: float= Field(gt=0)
    positions: list[tuple[float, float]]
    depth: float | Literal["through"]="through"

class CADPlan(BaseModel):
    part_name: str

    operation: Literal[
        "box",
        "plate",
        "bracket",
        "shaft",
        "custom"
    ]

    units: Literal["mm"]="mm"
    dimensions: dict[str, float]
    features: list[str]=[]
    holes: list[HoleSpec]=[]
    fillets: list[float]=[]
    chamfers: list[float]=[]
    expected_volume: float | None=None
    design_notes: list[str]=[]
    