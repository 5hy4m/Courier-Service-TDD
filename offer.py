class Offer:
    def __init__(self, offer):
        self.code = offer["code"]
        self.discount = offer["discount"]
        self.lower_limit_distance = offer["lower_limit_distance"]
        self.upper_limit_distance = offer["upper_limit_distance"]
        self.lower_limit_weight = offer["lower_limit_weight"]
        self.upper_limit_weight = offer["upper_limit_weight"]

    def isOfferCodeExist(self, offers):
        for offer in offers:
            if self.code == offer.code:
                return True
        else:
            return False

    def isOfferCodeValid(self, package_weight, package_distance):
        if not self.lower_limit_weight <= package_weight <= self.upper_limit_weight:
            return False
        if (
            not self.lower_limit_distance
            <= package_distance
            <= self.upper_limit_distance
        ):
            return False
        return True
