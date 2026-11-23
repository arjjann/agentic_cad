
from typing import TypedDict, NotRequired, Any


class CADState(TypedDict):
    # Original user request
    prompt: str

    # Structured design plan
    plan: NotRequired[dict[str, Any]]

    # Generated CadQuery Python script
    code: NotRequired[str]

    # Execution status and result
    execution_result: NotRequired[dict[str, Any]]

    # Geometry review
    review_result: NotRequired[dict[str, Any]]

    # Error history
    error_log: NotRequired[list[str]]

    # Retry counters
    script_retries: int
    design_retries: int

    # Final status
    status: str
