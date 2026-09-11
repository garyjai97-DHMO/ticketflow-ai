from ticketflow.change_detector import diff_ticket_ids


def test_detects_added_and_removed_ids():
    previous = {"TASK1001", "TASK1002"}
    current = {"TASK1002", "TASK1003"}

    result = diff_ticket_ids(previous, current)

    assert result.added == {"TASK1003"}
    assert result.removed == {"TASK1001"}


def test_no_changes():
    ids = {"TASK1001", "TASK1002"}

    result = diff_ticket_ids(ids, ids.copy())

    assert result.added == set()
    assert result.removed == set()


def test_inputs_are_not_mutated():
    previous = {"TASK1001"}
    current = {"TASK1002"}

    previous_before = previous.copy()
    current_before = current.copy()

    diff_ticket_ids(previous, current)

    assert previous == previous_before
    assert current == current_before
