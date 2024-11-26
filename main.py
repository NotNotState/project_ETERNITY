from functions.standard_deviation import standard_deviation
from functions.arccos import arccos_taylor
from functions.exponent import exponent
from functions.ab_power_x import ab_power_x
from functions.mean_absolute_deviation import get_mad
from functions.fancy_input import calc_obj
from functions.sinh import custom_sinh

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Type enforcement on front end requests
class DataModel(BaseModel):
    data : list[float] | str | float = None # This replaces that above

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Add async back if we need that 
@app.get("/")
def root():
    #return FileResponse(os.path.join(os.path.dirname(__file__), "../static/index.html")) # Run this if you get fucky behaviour
    #return FileResponse(os.path.join("static", "index.html"))
    return FileResponse("static/test_html/index.html")

@app.post("/calculate_call")
def process_calc_request(request : DataModel) -> dict:
    res = 0
    c = calc_obj()
    res = c.calculate(request.data)

    try:
        res = c.calculate(request.data)
    except:
        raise HTTPException(status_code=400, detail="data_operation not recognized")
    
    return {"calculation_result" : res}


if __name__ == "__main__":
    root()
