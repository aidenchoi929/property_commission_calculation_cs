from PropertyAgent import PropertyAgent

class PropertyAgencyDirector(PropertyAgent):
    def __init__(self, company, agent_registration_number, start_year, commission_sharing_rate=75, overriding_rate=5, director_name=""):
        super().__init__(company, agent_registration_number, start_year, commission_sharing_rate)
        self.overriding_rate = overriding_rate * 0.01
        self.director_name = director_name
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)
        agent.director = self  # Assign the director to the agent

    def add_property_sold(self, property):
        self.properties_sold.append(property)
        property.sold_by = self  # Track the director who sold the property

    def add_property_unsold(self, property):
        self.properties_unsold.append(property)
        property.unsold_by = self  # Track the director responsible for unsold property

    def calculate_overriding_income(self):
        total_overriding_income = 0
        for agent in self.agents:
            total_overriding_income += agent.calculate_total_commission() * self.overriding_rate
        return total_overriding_income

    def calculate_total_income(self):
        # Include income from agents and director's own sales
        return self.calculate_total_commission() + self.calculate_overriding_income()

    def count_agents_sold(self):
        total_sold_by_agents = 0
        for agent in self.agents:
            total_sold_by_agents += len(agent.properties_sold)
        return total_sold_by_agents
    def count_agents_unsold(self):
        total_unsold_by_agents = 0
        for agent in self.agents:
            total_unsold_by_agents += len(agent.properties_unsold)
        return total_unsold_by_agents