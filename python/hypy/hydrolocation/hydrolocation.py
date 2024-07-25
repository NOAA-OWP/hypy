from enum import Enum, auto
from typing import TYPE_CHECKING, Tuple, Union

if TYPE_CHECKING:
    from shapely.geometry import Point

class HydroLocationType(Enum):
    """
        Enumeration of hydro location types
    """
    UNDEFINED = auto()
    barrage = auto()
    bifurcation = auto()
    catchmentOutlet = auto()
    confluence = auto()
    dam = auto()
    diversionOfWater = auto()
    extractionWell = auto()
    fork = auto()
    hydrometricStation = auto()
    infiltrationWell = auto()
    injectionWell = auto()
    inletStructure = auto()
    intake = auto()
    outletStructure = auto()
    ponor = auto()
    pourPoint = auto()
    rapids = auto()
    refenceClimatologicalStation = auto()
    riverMouth = auto()
    sinkhole = auto()
    source = auto()
    spring = auto()
    waterfall = auto()
    weir = auto()

class HydroLocation():
    """
        Implementation of the HY Features HydroLocation concept
    """
    __slots__ = ['_shape', '_type', '_referenced_position', '_realized_nexus']

    def __init__(self,
                realized_nexus: str,
                shape: Union['Point', Tuple] = None,
                type: HydroLocationType = HydroLocationType.UNDEFINED,
                referenced_position = None, #TODO implement indirect position?
                ):
        """

        Parameters
        ----------
        shape: Union[Point, Tuple]
            a shapely point geometry or two-tuple defining the coordinates of this location
        type: HydroLocationType
            enum value defining the type of feature at this location
        referenced_position:
            position expressed as measured or otherwise described distance from a known, already located referent
        realized_nexus: str
            the nexus identifier associated with this location
        """
        self._shape = shape
        self._type = type
        self._referenced_position = referenced_position
        self._realized_nexus = realized_nexus

    @property
    def realized_nexus(self) -> str:
        """
            string identifer of the nexus this location realizes
        """
        return self._realized_nexus

    @property
    def geometry(self) -> Union['Point', Tuple]:
        """
            Geometric coordinates of the location as a `Point` or two-Tuple
        """
        return self._shape

    @property
    def ltype(self) -> HydroLocationType:
        """
            Location type
        """
        return self._type
