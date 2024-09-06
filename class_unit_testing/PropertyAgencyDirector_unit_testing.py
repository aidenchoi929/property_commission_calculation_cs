from Property import Property
from PropertyAgent import PropertyAgent
from PropertyAgencyDirector import PropertyAgencyDirector

# Example properties
property1 = Property(address="1 Lorong 5 Toa Payoh",postal_code="349574",tenure="Freehold",completion_year=2010,property_type="Residential",area=1200,valuation=1000000)

# Example property agent
agent = PropertyAgent(company="PropNex",agent_registration_number="A098",start_year=2024,commission_sharing_rate=70,agent_name="Aiden Choi")

# Example property agency director
director = PropertyAgencyDirector(company="PropNex",agent_registration_number="D111",start_year=2010,commission_sharing_rate=75,overriding_rate=10,director_name="Andrew Choi")

# Adding the agent to the director
director.add_agent(agent)

# Adding properties sold by the agent
agent.add_property_sold(property1)

# Calculate total income earned by the director
total_income = director.calculate_total_income()

# Print the director details and total income
print(f"Director Details:\n"
      f"Company: {director.company}\n"
      f"Director Name: {director.director_name}\n"
      f"Agent Registration Number: {director.agent_registration_number}\n"
      f"Start Year: {director.start_year}\n"
      f"Commission Sharing Rate: {director.commission_sharing_rate * 100}%\n"
      f"Overriding Rate: {director.overriding_rate * 100}%\n"
      f"Total Income: ${total_income:.2f}")

# Print the properties sold by the director and agents
print("\nProperties Sold by Agents:")
for agent in director.agents:
    for property in agent.properties_sold:
        commission = property.calculate_commission()
        print(f"\nAgent: {agent.agent_name}\n"
              f"Address: {property.address}\n"
              f"Postal Code: {property.postal_code}\n"
              f"Tenure: {property.tenure}\n"
              f"Completion Year: {property.completion_year}\n"
              f"Property Type: {property.property_type}\n"
              f"Area: {property.area} sq ft\n"
              f"Valuation: ${property.valuation}\n"
              f"Commission Rate: {property.commission_rate * 100}%\n"
              f"Commission: ${commission:.2f}")
