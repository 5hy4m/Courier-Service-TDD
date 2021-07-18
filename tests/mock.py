from constants import PACKAGES_ARRAY_OF_OBJECTS


class InputMock:
    def execute(mock_input, data=None):
        if data is "packages":
            mock_input.side_effect = [
                "PKG1 5 5 OFR001",
                "PKG2 15 5 OFR002",
                "PKG3 10 100 OFR003",
            ]
        elif data is "algorithm":
            mock_input.side_effect = [
                "100 4",
                "PKG1 1 5 OFR001",
                "PKG2 1 5 OFR002",
                "PKG3 2 100 OFR003",
                "PKG3 4 100 OFR003",
                "2 4 4",
            ]
        else:
            mock_input.side_effect = [
                "100 3",
                "PKG1 5 5 OFR001",
                "PKG2 15 5 OFR002",
                "PKG3 10 100 OFR003",
                "2 70 200",
            ]
