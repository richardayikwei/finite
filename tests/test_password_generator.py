from src import password_engine, InputTooSmallError
import pytest

class TestErrors:
    def test_input_too_small_error(self):
        with pytest.raises(InputTooSmallError):
            password_engine(9)
