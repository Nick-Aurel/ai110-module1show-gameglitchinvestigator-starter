import pytest

from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_rejects_blank():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None


@pytest.mark.parametrize(
    "raw",
    [
        None,
        "",
        "   ",
        "not a number",
        "1e3",
    ],
)
def test_parse_guess_rejects_invalid_inputs(raw):
    ok, value, err = parse_guess(raw)
    assert ok is False
    assert value is None
    assert err is not None


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("5", 5),
        ("  5  ", 5),
        ("12.7", 12),  # decimals get truncated via int(float(...))
        ("-3", -3),
    ],
)
def test_parse_guess_accepts_integers_and_decimals(raw, expected):
    ok, value, err = parse_guess(raw)
    assert ok is True
    assert value == expected
    assert err is None


def test_parse_guess_accepts_very_large_integer():
    raw = "999999999999999999999999999999"
    ok, value, err = parse_guess(raw)
    assert ok is True
    assert isinstance(value, int)
    assert value > 10**10
    assert err is None
