from tabulate import tabulate
from Property import Property
from PropertyAgent import PropertyAgent
from PropertyAgencyDirector import PropertyAgencyDirector
from CommissionSlip import CommissionSlip

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

# Adding properties to commission slip
commission_slip = CommissionSlip()
commission_slip.add_property(property1)
commission_slip.add_agent(agent)
commission_slip.add_director(director)

# Print the properties and agents/directors
commission_slip.print_properties()
commission_slip.print_agents_directors()
