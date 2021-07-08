PACKAGES_ARRAY_OF_OBJECTS = [
    {
        "id": "PKG1",
        "weight": 5,
        "distance": 5,
        "offer_code": "OFR001",
    },
    {
        "id": "PKG2",
        "weight": 15,
        "distance": 5,
        "offer_code": "OFR002",
    },
    {
        "id": "PKG3",
        "weight": 10,
        "distance": 100,
        "offer_code": "OFR003",
    },
]

OFFERS_ARRAY_OF_OBJECTS = [
    {
        "code": "OFR001",
        "discount": "10",
        "lower_limit_distance": "0",
        "upper_limit_distance": "200",
        "lower_limit_weight": "70",
        "upper_limit_weight": "200",
    },
    {
        "code": "OFR002",
        "discount": "7",
        "lower_limit_distance": "50",
        "upper_limit_distance": "150",
        "lower_limit_weight": "100",
        "upper_limit_weight": "250",
    },
    {
        "code": "OFR003",
        "discount": "5",
        "lower_limit_distance": "50",
        "upper_limit_distance": "250",
        "lower_limit_weight": "10",
        "upper_limit_weight": "150",
    },
]

PARSED_OFFERS_ARRAY_OF_OBJECTS = [
    {
        "code": "OFR001",
        "discount": 10.0,
        "lower_limit_distance": 0,
        "upper_limit_distance": 200,
        "lower_limit_weight": 70,
        "upper_limit_weight": 200,
    },
    {
        "code": "OFR002",
        "discount": 7.0,
        "lower_limit_distance": 50,
        "upper_limit_distance": 150,
        "lower_limit_weight": 100,
        "upper_limit_weight": 250,
    },
    {
        "code": "OFR003",
        "discount": 5.0,
        "lower_limit_distance": 50,
        "upper_limit_distance": 250,
        "lower_limit_weight": 10,
        "upper_limit_weight": 150,
    },
]

OUTPUT = """PKG1 0 175
PKG2 0 275
PKG3 35 665
"""

ARRAY_2D = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

BUILT2DARRAY = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 5],
    [0, 0, 0, 3, 3, 5, 5],
    [0, 0, 0, 3, 4, 5, 5],
    [0, 0, 2, 3, 4, 5, 6],
]

SOLVED_ARRAY = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 2, 2, 2],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
]
