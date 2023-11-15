from time import sleep as wait
dataType = str | int | float | bool | list | tuple | set | dict


class Expect:
    """
    Utility class for performing assertions and validations on various data types.
    """

    def __init__(self, actualValue: dataType):
        """
        Initializes the Expect object with the actual value to be tested.

        Args:
            actual_value: The value against which assertions will be made.
        """
        if not isinstance(actualValue, dataType):
            raise ValueError(f'DataType not supported. try: {dataType}')
        self.value = actualValue
        self.dataType = dataType

    def toBeEqual(self, expectedValue: dataType) -> None:
        if not isinstance(expectedValue, dataType):
            raise ValueError(f'DataType not supported. try: {dataType}')
        assert self.value == expectedValue
        wait(1)

    def toNotBeEqual(self, expectedValue: dataType) -> None:
        if not isinstance(expectedValue, dataType):
            raise ValueError(f'DataType not supported. try: {dataType}')
        assert self.value != expectedValue
        wait(1)

    def toContain(self, innerValue: str) -> None:
        if not isinstance(self.value, str):
            raise ValueError(f'Value type not supported. Use String type')
        assert innerValue in self.value
        wait(1)

    def isTrue(self) -> None:
        if not isinstance(self.value, bool):
            raise ValueError(f'Value type not supported. Use Boolean type')
        assert self.value == True
        wait(1)

    def isFalse(self) -> None:
        if not isinstance(self.value, bool):
            raise ValueError(f'Value type not supported. Use Boolean type')
        assert self.value == False
        wait(1)
