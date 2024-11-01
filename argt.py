from typing import TypedDict, Any

class Options(TypedDict, total=False):
    age_limit: int
    land_codes: list[int]

class Options2:
    age_limit: int
    land_codes: list[int]

def is_eligible(data: str, options: Options2) -> Any:
    age_limit : int = options.get("age_limit", 0)

    return age_limit


v = is_eligible('Hi', {"age_limit": 10})
print(v)