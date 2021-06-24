class Offer:
    def __init__(self, offer):
        self.code = offer["code"]
        self.discount = offer["discount"]
        self.lower_limit_distance = offer["lower_limit_distance"]
        self.upper_limit_distance = offer["upper_limit_distance"]
        self.lower_limit_weight = offer["lower_limit_weight"]
        self.upper_limit_weight = offer["upper_limit_weight"]
