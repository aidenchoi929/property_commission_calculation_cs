class Property:
    def __init__(self, address, postal_code, tenure, completion_year, property_type, area, valuation, commission_rate=0.01):
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.valuation = valuation
        self.commission_rate = commission_rate
        self.sold_by = None  # Added to track the agent or director who sold the property
        self.unsold_by = None  # Added to track the agent or director responsible for unsold property

    def calculate_commission(self):
        return self.valuation * self.commission_rate

