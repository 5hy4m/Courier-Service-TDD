PACKAGES_ARRAY_OF_OBJECTS = [
    {
        "id": "PKG1",
        "weight_in_kg": 5,
        "distance_in_km": 5,
        "offer_code": "OFR001",
    },
    {
        "id": "PKG2",
        "weight_in_kg": 15,
        "distance_in_km": 5,
        "offer_code": "OFR002",
    },
    {
        "id": "PKG3",
        "weight_in_kg": 10,
        "distance_in_km": 100,
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
