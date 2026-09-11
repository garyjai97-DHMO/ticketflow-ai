from dataclasses import dataclass


@dataclass(frozen=True)
class TicketDiff:
    added: set[str]
    removed: set[str]


def diff_ticket_ids(previous: set[str], current: set[str]) -> TicketDiff:
    """Compare two snapshots of ticket IDs.

    TODO: implement this function by hand.

    Requirements:
    - added = IDs only in current
    - removed = IDs only in previous
    - do not mutate either input set
    """
    raise NotImplementedError("Implement diff_ticket_ids as your first coding task.")
