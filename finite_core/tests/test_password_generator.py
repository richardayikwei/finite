from finite_core.src import password_engine, InputTooSmallError
import pytest

class TestErrors:
    def test_input_too_small_error(self):
        with pytest.raises(InputTooSmallError):
            password_engine(9)

    def test_input_is_a_float_error(self):
        with pytest.raises(TypeError):
            password_engine(10.5)
