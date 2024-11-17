from functions.standard_deviation import standard_deviation
from functions.arccos import arccos_taylor
from functions.exponent import exponent
from functions.ab_power_x import ab_power_x
from functions.mean_absolute_deviation import get_mad
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Type enforcement on front end requests
class DataModel(BaseModel):
    data : list[float] | str | float = None # This replaces that above
    data_operation: str | None = None

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Add async back if we need that 
@app.get("/")
def root():
    #return FileResponse(os.path.join(os.path.dirname(__file__), "../static/index.html")) # Run this if you get fucky behaviour
    #return FileResponse(os.path.join("static", "index.html"))
    return FileResponse("static/index.html")

@app.post("/calculate_call")
def process_calc_request(request : DataModel) -> dict:
    res = 0
    
    func = dict(
        standard_deviation = standard_deviation,
        mean_absolute_deviation = get_mad(),
        gamma_function = lambda x : x,
        arccos = arccos_taylor(),
        power_function = exponent,
        log_function = lambda x : x,
        exponential_growth = ab_power_x,
        arithmetic_expression = lambda x : eval(x, {}, {}),
    ).get(request.data_operation, None)

    try:
        res = func(request.data)
    except:
        raise HTTPException(status_code=400, detail="data_operation not recognized")
    
    return {"calculation_result" : res}


if __name__ == "__main__":
    root()

    x = -1  # Example input in the range [-1, 1]
    result = arccos_taylor(x)
    print("arccos(", x, ") =", result)
