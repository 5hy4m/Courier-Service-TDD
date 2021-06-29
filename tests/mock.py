from constants import PACKAGES_ARRAY_OF_OBJECTS


class InputMock:
    def execute(mock_input):
        mock_input.side_effect = [
            "100 3",
            "PKG1 5 5 OFR001",
            "PKG2 15 5 OFR002",
            "PKG3 10 100 OFR003",
        ]
