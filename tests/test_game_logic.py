from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_go_lower():
    # Guess too high should tell player to go lower
    outcome, message = check_guess(80, 50)
    assert "LOWER" in message


def test_hint_go_higher():
    # Guess too low should tell player to go higher
    outcome, message = check_guess(20, 50)
    assert "HIGHER" in message


def test_score_win():
    # Winning should increase score
    new_score = update_score(0, "Win", 1)
    assert new_score > 0


def test_score_wrong_guess():
    # Wrong guess should decrease score by 5
    new_score = update_score(0, "Too High", 1)
    assert new_score == -5


def test_parse_valid_guess():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42


def test_parse_empty_guess():
    ok, value, err = parse_guess("")
    assert ok == False


def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20
