from fastapi import APIRouter, Depends, Response
from typing import List, Union, Optional
from queries.locations import (
    LocationIn,
    LocationOut,
    LocationRepository,
    Error,
    AllLocationsOut,
)
from pydantic import BaseModel

router = APIRouter()


class HttpError(BaseModel):
    detail: str


# GET all locations
@router.get(
    "/api/locations/", response_model=Union[List[AllLocationsOut], Error]
)
def get_all(
    repo: LocationRepository = Depends(),
):
    return repo.get_all()


# POST create new location
@router.post("/api/locations/", response_model=Union[LocationOut, Error])
def create_location(
    location: LocationIn,
    repo: LocationRepository = Depends(),
):
    return repo.create_location(location)


@router.put(
    "/api/locations/{location_id}", response_model=Union[LocationOut, Error]
)
def update_location(
    location_id: int,
    location: LocationIn,
    repo: LocationRepository = Depends(),
) -> Union[Error, LocationOut]:

    updated_location = repo.update_location(location_id, location)
    return updated_location


@router.delete("/api/locations/{location_id}", response_model=bool)
def delete_location(
    location_id: int,
    repo: LocationRepository = Depends(),
) -> bool:
    return repo.delete_location(location_id)


@router.get(
    "/api/locations/{location_id}", response_model=Optional[LocationOut]
)
def get_location_singular(
    location_id: int,
    response: Response,
    repo: LocationRepository = Depends(),
) -> LocationOut:
    location = repo.get_singular(location_id)
    if location is None:
        response.status_code = 404
    return location
