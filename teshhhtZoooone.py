from pydantic import BaseModel

class DataModel(BaseModel):
    data : list[float] | str | float = None # This replaces that above
    data_operation: str | None = None

def test_map(request):

    func = dict(
        standard_deviation = lambda x : x,
        mean_absolute_deviation = lambda x : -x,
        gamma_function = lambda x : x,
        arccos = lambda x : x,
        power_function = lambda x : x,
        log_function = lambda x : x,
        exponential_growth = lambda x : x,
        arithmetic_operation = lambda x : x,
    ).get(request.data_operation, None)

    return func(request.data) if func != -1 else None

if __name__ == "__main__":
    test_req = {
        "data_operation" : "standard_deviation",
        "data" : -100
    }

    test_req = DataModel()
    test_req.data_operation = "mean_absolute_deviation"
    test_req.data = -100

    print(test_map(test_req))

