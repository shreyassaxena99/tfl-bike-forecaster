from pydantic import BaseModel 

class BikePoint(BaseModel):
    """
    A BikePoint is a physical location where TfLbikes can be rented and returned.
    It is identified by a unique ID and has a name, latitude, longitude, and terminal name.
    It also has a a number of attributes that describe the current state of the bike point.
    """
    id: str
    name: str
    lat: float
    long: float
    terminalName: int
    timestamp: int
    installed: bool
    locked: bool
    installDate: int
    removalDate: float
    temporary: bool
    nbBikes: int
    nbEmptyDocks: int
    nbDocks: int
    nbStandardBikes: int 
    nbEBikes: int