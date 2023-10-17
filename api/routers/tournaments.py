from fastapi import APIRouter, Depends
from typing import Union, List
from queries.tournaments import (
    TournamentIn,
    TournamentOut,
    TournamentOutWithLocation,
    TournamentRepository,
    Error,
)


router = APIRouter()


@router.post("/api/tournaments", response_model=Union[TournamentOut, Error])
def create_tournament(
    tournament: TournamentIn,
    repo: TournamentRepository = Depends(),
):
    return repo.create(tournament)


@router.get(
    "/api/tournaments",
    response_model=Union[List[TournamentOutWithLocation], Error],
)
def get_all(
    repo: TournamentRepository = Depends(),
):
    return repo.get_all()


@router.put(
    "/api/tournaments/{tournament_id}",
    response_model=Union[TournamentOut, Error],
)
def update_tournament(
    tournament_id: int,
    tournament: TournamentIn,
    repo: TournamentRepository = Depends(),
) -> Union[TournamentOut, Error]:
    return repo.update(tournament_id, tournament)


@router.get(
    "/api/tournaments/{tournament_id}",
    response_model=Union[TournamentOutWithLocation, Error],
)
def get_specific_tournament(
    tournament_id: int,
    repo: TournamentRepository = Depends(),
) -> TournamentOutWithLocation:
    return repo.get_specific(tournament_id)


@router.delete(
    "/api/tournaments/{tournament_id}",
    response_model=bool,
)
def delete_tournament(
    tournament_id: int,
    repo: TournamentRepository = Depends(),
) -> bool:
    return repo.delete_tournament(tournament_id)
