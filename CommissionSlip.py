from tabulate import tabulate
from PropertyAgencyDirector import PropertyAgencyDirector

# Class to handle lists and tabulate output
class CommissionSlip:
    def __init__(self):
        self.properties = []
        self.agents = []
        self.directors = []

    def add_property(self, property):
        self.properties.append(property)

    def add_agent(self, agent):
        self.agents.append(agent)

    def add_director(self, director):
        self.directors.append(director)

    def print_properties(self):
        data = []
        for idx, property in enumerate(self.properties, 1):
            if property.sold_by:
                seller_commission = property.calculate_commission() * property.sold_by.commission_sharing_rate
                if isinstance(property.sold_by, PropertyAgencyDirector):
                    director_commission = "N/A"  # Director's own sales don't have overriding fee
                    override_fee = "N/A"
                    contact_name = property.sold_by.director_name
                else:
                    director_commission = int(seller_commission * property.sold_by.director.overriding_rate) if property.sold_by.director else 0
                    override_fee = int(property.sold_by.director.overriding_rate * 100) if property.sold_by.director else ""
                    contact_name = property.sold_by.agent_name

                row = [
                    idx,
                    property.address,
                    property.postal_code,
                    property.tenure,
                    property.completion_year,
                    property.property_type,
                    property.area,
                    property.valuation,
                    "Sold",
                    contact_name,
                    property.sold_by.agent_registration_number,
                    int(property.sold_by.commission_sharing_rate * 100),
                    int(seller_commission),
                    "" if isinstance(property.sold_by, PropertyAgencyDirector) else property.sold_by.director.director_name if property.sold_by.director else "",
                    "" if isinstance(property.sold_by, PropertyAgencyDirector) else property.sold_by.director.agent_registration_number if property.sold_by.director else "",
                    override_fee,
                    director_commission
                ]
            else:
                row = [
                    idx,
                    property.address,
                    property.postal_code,
                    property.tenure,
                    property.completion_year,
                    property.property_type,
                    property.area,
                    property.valuation,
                    "Unsold",
                    property.unsold_by.agent_name if property.unsold_by else "",
                    property.unsold_by.agent_registration_number if property.unsold_by else "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            data.append(row)
        
        headers = [
            "#", "Address", "Postal Code", "Tenure", "Year", "Type", "Area",
            "Value($)", "Status", "Sold agent/director", "Reg No", "Commission Rate(%)", "Commission($)",
            "Director", "Director Reg No", "Overriding rate(%)", "Overriding fee($)"
        ]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def print_agents_directors(self):
        data = []

        for agent in self.agents:
            data.append([
                agent.agent_name,
                agent.agent_registration_number,
                agent.company,
                agent.start_year,
                "Agent",
                len(agent.properties_sold),
                len(agent.properties_unsold),
                int(agent.calculate_total_commission()),
                ""
            ])
        
        for director in self.directors:
            data.append([
                director.director_name,
                director.agent_registration_number,
                director.company,
                director.start_year,
                "Director",
                len(director.properties_sold),
                director.count_agents_unsold(),
                int(director.calculate_total_income()),  # Include income from agents
                director.count_agents_sold()
            ])

        headers = ["Name", "Reg No", "Company", "Start Year", "Role", "Property Sold", "Property Unsold", "Total Commission($)", "Agents Sold"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

