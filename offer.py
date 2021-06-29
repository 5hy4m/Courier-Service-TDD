class Offer:
    def __init__(self, offer):
        self.code = offer["code"]
        self.discount = offer["discount"]
        self.lower_limit_distance = offer["lower_limit_distance"]
        self.upper_limit_distance = offer["upper_limit_distance"]
        self.lower_limit_weight = offer["lower_limit_weight"]
        self.upper_limit_weight = offer["upper_limit_weight"]

    @staticmethod
    def isOfferCodeExist(package_offer, offers):
        for offer in offers:
            if package_offer.code == offer.code:
                return True
        else:
            return False

    @staticmethod
    def isOfferCodeValid(package):
        offer = package.offer_code
        if (
            not offer.lower_limit_distance
            <= package.distance
            <= offer.upper_limit_distance
        ):
            return False
        if not offer.lower_limit_weight <= package.weight <= offer.upper_limit_weight:
            return False
        return True
