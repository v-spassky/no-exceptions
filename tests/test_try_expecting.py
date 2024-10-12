import pytest
from src.no_exceptions import try_expecting


def test_try_expecting_success() -> None:
    numerator = 42
    denominator = 6
    result = try_expecting(lambda: numerator / denominator, ZeroDivisionError)
    assert result.is_ok
    assert isinstance(result._inner, float)
    assert result.unwrap() == 7.0
    assert result.unwrap_or(0) == 7.0
    assert result.unpack() == (True, 7.0)


def test_try_expecting_failure() -> None:
    numerator = 1
    denominator = 0
    result = try_expecting(lambda: numerator / denominator, ZeroDivisionError)
    assert result.is_err
    assert isinstance(result._inner, ZeroDivisionError)
    with pytest.raises(ValueError):
        result.unwrap()
    assert result.unwrap_or(0) == 0
    assert result.unpack() == (False, None)


def test_try_expecting_with_exception_instnace() -> None:
    result = try_expecting(lambda: AttributeError(), ZeroDivisionError)
    assert result.is_ok
    assert isinstance(result._inner, AttributeError)


def test_try_expecting_with_exception_instnace2() -> None:
    result = try_expecting(lambda: FloatingPointError(), ArithmeticError)
    assert result.is_ok
    assert isinstance(result._inner, FloatingPointError)
