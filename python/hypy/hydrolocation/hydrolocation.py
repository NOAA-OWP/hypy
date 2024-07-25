from enum import Enum
from typing import TYPE_CHECKING, Tuple, Union

if TYPE_CHECKING:
    from shapely.geometry import Point

class HydroLocationType(Enum):
    """
        Enumeration of hydro location types
    """
    UNDEFINED = ()
    barrage = ()
    bifurcation = ()
    catchmentOutlet = ()
    confluence = ()
    dam = ()
    diversionOfWater = ()
    extractionWell = ()
    fork = ()
    hydrometricStation = ()
    infiltrationWell = ()
    injectionWell = ()
    inletStructure = ()
    intake = ()
    outletStructure = ()
    ponor = ()
    pourPoint = ()
    rapids = ()
    refenceClimatologicalStation = ()
    riverMouth = ()
    sinkhole = ()
    source = ()
    spring = ()
    waterfall = ()
    weir = ()

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
