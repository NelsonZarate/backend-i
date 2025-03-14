from typer.testing import CliRunner
from pytest import raises
import pytest
runner = CliRunner()

from src.session_8.app import app


@pytest.fixture
def command_test_int():
    return runner.invoke(app,["2"])

@pytest.fixture
def command_test_str():
    return runner.invoke(app,["str"])


def test_app_int(command_test_int):
    result = command_test_int
    assert "4" in result.stdout

def test_app_str(command_test_str):
    result = command_test_str
    with raises(AssertionError):
        assert "TypeError" in result.stdout