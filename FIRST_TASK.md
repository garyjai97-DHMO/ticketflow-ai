# First Task — Ticket State Change Detection

This is intentionally the first part of TicketFlow AI that Gary should write by hand.

The purpose is not to solve a difficult algorithm problem. The purpose is to rebuild Python fluency using logic that belongs to the real project.

## Requirement

Open:

`src/ticketflow/change_detector.py`

Implement:

```python
def diff_ticket_ids(previous: set[str], current: set[str]) -> TicketDiff:
```

It should return:

- `added`: ticket IDs that exist in `current` but not `previous`
- `removed`: ticket IDs that exist in `previous` but not `current`

Example:

```python
previous = {"TASK1001", "TASK1002"}
current = {"TASK1002", "TASK1003"}

# Expected:
added == {"TASK1003"}
removed == {"TASK1001"}
```

## Constraints

- Do not mutate either input set.
- Make the first implementation yourself rather than asking an AI agent to generate it.
- Looking up Python syntax is fine.
- After writing it, run the tests and make sure you can explain why the solution works.

## Run the tests

After setting up the project environment:

```bash
pytest -q
```

The goal is for all tests to pass.

## Engineering question for later

The first implementation treats a missing ticket as `removed`, but a production system should **not automatically assume that one missing poll means the ticket is definitely closed**.

Later we will discuss why a ticket might temporarily disappear and how to design safer state semantics.
