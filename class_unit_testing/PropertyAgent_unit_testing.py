from Property import Property
from PropertyAgent import PropertyAgent

# Example properties
property1 = Property(address="1 Lorong 5 Toa Payoh",postal_code="349574",tenure="Freehold",completion_year=2010,property_type="Residential",area=1200,valuation=1000000)

# Example property agent
agent = PropertyAgent(company="PropNex",agent_registration_number="A098",start_year=2024,commission_sharing_rate=70,agent_name="Aiden Choi")

# Adding properties sold by the agent
agent.add_property_sold(property1)

# Calculate total commission earned by the agent
total_commission = agent.calculate_total_commission()

# Print the agent details and total commission
print(f"Agent Details:\n"
      f"Company: {agent.company}\n"
      f"Agent Name: {agent.agent_name}\n"
      f"Agent Registration Number: {agent.agent_registration_number}\n"
      f"Start Year: {agent.start_year}\n"
      f"Commission Sharing Rate: {agent.commission_sharing_rate * 100}%\n"
      f"Total Commission: ${total_commission:.2f}")

# Print the properties sold by the agent
print("\nProperties Sold:")
for property in agent.properties_sold:
    commission = property.calculate_commission()
    print(f"\nAddress: {property.address}\n"
          f"Postal Code: {property.postal_code}\n"
          f"Tenure: {property.tenure}\n"
          f"Completion Year: {property.completion_year}\n"
          f"Property Type: {property.property_type}\n"
          f"Area: {property.area} sq ft\n"
          f"Valuation: ${property.valuation}\n"
          f"Commission Rate: {property.commission_rate * 100}%\n"
          f"Commission: ${commission:.2f}")
