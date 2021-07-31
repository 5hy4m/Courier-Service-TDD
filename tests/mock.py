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
        elif data is "vehicle_allocation":
            mock_input.side_effect = [
                "100 5",
                "PKG1 50 30 OFR001",
                "PKG2 75 125 OFFR0008",
                "PKG3 175 100 OFFR003",
                "PKG4 110 60 OFR002",
                "PKG5 155 95 NA",
                "2 70 200",
            ]
        elif data is "algorithm_with_weight":
            mock_input.side_effect = [
                "100 3",
                "PKG1 5 30 OFR001",
                "PKG5 9 95 NA",
                "PKG3 7 100 OFFR003",
                "1 70 10",
            ]
        else:
            mock_input.side_effect = [
                "100 3",
                "PKG1 5 5 OFR001",
                "PKG2 15 5 OFR002",
                "PKG3 10 100 OFR003",
                "2 70 200",
            ]
