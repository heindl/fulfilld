# Fulfilld Coding Exercise 

## Description

You have two players, Bob and Alice, that take turns in rolling a fair k-sided die. 
Whoever rolls a k first wins the game. 
The Python program should output the probability that Bob wins the game for k=6 through 99. 
That is, the output will be an array of probabilities where index 0 is the probability when k = 6; index 1 when k = 7; etc.

## Installation

The project relies on a [Taskfile](https://taskfile.dev/installation/) for build automation. The following commands are available:
- `task install` - If necessary, install a virtual environment and dependencies.
- `task upgrade` - Upgrade dependencies.
- `task lint` - Lint project with ruff and mypy.
- `task test` - Execute unit tests.
- `task run` - Run the fastapi web server locally on port 8080. 

There is also a Docker Compose file available to run the project in a container, also on port 8080:
```bash
docker-compose up
```

To test the API, you can use the following curl commands:
```bash
# Return the list of probabilities.
curl http://localhost:8080
# Return the probability of a given dice.
curl -H "k: 9" http://localhost:8080
```