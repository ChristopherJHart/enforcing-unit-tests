# Granular Enforcement of Python Unit Test Coverage through Code Inspection

This repository tracks a Proof of Concept (PoC) where we use code inspection to enforce granular unit test coverage for a Python software application that may grow in size and complexity over time.

A blog post that explains this concept in more detail can be found [here](https://chrisjhart.com/Enforcing-Python-Unit-Test-Coverage/).

## Getting Started

Create a new Python virtual environment:

```shell
python3 -m venv venv
```

Activate the new Python virtual environment:

```shell
source venv/bin/activate
```

Install dependencies through the `requirements.txt` file:

```shell
pip3 install -r requirements.txt
```

Finally, run unit tests and experiment with the code to demonstrate how this code works.

```shell
python3 -m pytest
```
