class PropertyAgent:
    def __init__(self, company, agent_registration_number, start_year, commission_sharing_rate=70, agent_name=""):
        self.company = company
        self.agent_name = agent_name
        self.agent_registration_number = agent_registration_number
        self.start_year = start_year
        self.commission_sharing_rate = commission_sharing_rate * 0.01
        self.properties_sold = []
        self.properties_unsold = []
        self.director = None  # Added to track the director

    def add_property_sold(self, property):
        self.properties_sold.append(property)
        property.sold_by = self  # Track the agent who sold the property

    def add_property_unsold(self, property):
        self.properties_unsold.append(property)
        property.unsold_by = self  # Track the agent responsible for unsold property

    def calculate_total_commission(self):
        total_commission = 0
        for property in self.properties_sold:
            total_commission += property.calculate_commission() * self.commission_sharing_rate
        return total_commission

    def calculate_director_commission(self):
        if self.director:
            return self.calculate_total_commission() * self.director.overriding_rate
        return 0