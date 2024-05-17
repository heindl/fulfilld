from typing import Annotated

from fastapi import FastAPI, Header, HTTPException

MIN_K = 6
MAX_K = 99


def calculate_probability(k: int) -> float:
    """Two players are taking turns rolling a k-sided dice. The first to roll a k wins.
    Return the probability that the initial player wins."""
    return (1 / k) / (1 - ((k - 1) / k) ** 2)


def calculate_probabilities() -> list[float]:
    return [calculate_probability(k) for k in range(MIN_K, MAX_K + 1)]


app = FastAPI()


@app.get("/", response_model=list[float] | float)
def main_route(k: Annotated[int | None, Header()] = None):
    if k is not None:
        if k < MIN_K or k > MAX_K:
            raise HTTPException(
                status_code=400,
                detail=f"k must be between {MIN_K} and {MAX_K}",
            )
        return calculate_probability(k)
    return calculate_probabilities()


@app.get("/status", response_model=str)
def status_route():
    return "ok"
