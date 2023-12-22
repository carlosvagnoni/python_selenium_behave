from time import sleep as wait
data_type = str | int | float | bool | list | tuple | set | dict


class Expect:
    """
    Utility class for performing assertions and validations on various data types.
    """

    def __init__(self, actual_value: data_type):
        """
        Initializes the Expect object with the actual value to be tested.

        Args:
            actual_value: The value against which assertions will be made.
        """
        if not isinstance(actual_value, data_type):
            raise ValueError(f'DataType not supported. try: {data_type}')
        self.value = actual_value
        self.data_type = data_type

    def to_be_equal(self, expected_value: data_type) -> None:
        if not isinstance(expected_value, data_type):
            raise ValueError(f'DataType not supported. try: {data_type}')
        assert self.value == expected_value
        wait(1)

    def to_not_be_equal(self, expected_value: data_type) -> None:
        if not isinstance(expected_value, data_type):
            raise ValueError(f'DataType not supported. try: {data_type}')
        assert self.value != expected_value
        wait(1)

    def to_contain(self, inner_value: str) -> None:
        if not isinstance(self.value, str):
            raise ValueError('Value type not supported. Use String type')
        assert inner_value in self.value
        wait(1)

    def is_true(self) -> None:
        if not isinstance(self.value, bool):
            raise ValueError('Value type not supported. Use Boolean type')
        assert self.value == True
        wait(1)

    def is_false(self) -> None:
        if not isinstance(self.value, bool):
            raise ValueError('Value type not supported. Use Boolean type')
        assert self.value == False
        wait(1)
