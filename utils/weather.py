from pydantic import BaseModel


class Weather(BaseModel):
    status : str
    description : str
    icon : str
    temp : float
    temp_min : float
    temp_max : float
    wind_speed : float
    dt : int
    humidity : int
    sunrise : int
    sunset : int
    
    