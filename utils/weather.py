from pydantic import BaseModel


class Weather(BaseModel):
    status : str
    description : str
    icon : str
    temp : int
    temp_min : int
    temp_max : int
    wind_speed : float
    dt : int
    sunrise : int
    sunset : int
    
    