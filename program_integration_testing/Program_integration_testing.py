from tabulate import tabulate
from Property import Property
from CommercialProperty import CommercialProperty
from PropertyAgent import PropertyAgent
from PropertyAgencyDirector import PropertyAgencyDirector
from CommissionSlip import CommissionSlip

# Example Usage
def main():
    # Create an agency
    agency = CommissionSlip()
    
    # Create a director
    director = PropertyAgencyDirector(company="Propnex", agent_registration_number="D123", start_year=2000, commission_sharing_rate=75, overriding_rate=10, director_name="Titus Ong")
    director2 = PropertyAgencyDirector(company="ERA", agent_registration_number="D456", start_year=2004, commission_sharing_rate=75, overriding_rate=15, director_name="Ben Foo")

    # Create a property agent and assign the director
    agent1 = PropertyAgent(company= "Propnex", agent_registration_number ="A123", start_year = 2012, commission_sharing_rate=70, agent_name="Lim Wei")
    agent2 = PropertyAgent(company= "Propnex", agent_registration_number ="A345", start_year = 2011, commission_sharing_rate=70, agent_name="Tan Mei")
    agent3 = PropertyAgent(company= "ERA", agent_registration_number ="A678", start_year = 2015, commission_sharing_rate=70, agent_name="Ong Jun")
    director.add_agent(agent1)
    director.add_agent(agent2)
    director2.add_agent(agent3)

    # Add unsold properties that managed by director and sold
    drp1 = Property(address="789 Pine St", postal_code=789012, tenure="Freehold", completion_year=2021, property_type="Residential", area=1300, valuation=450000, commission_rate=0.01)

    # Changed to director selling the property
    director.add_property_sold(drp1)

    # Add sold properties by director to agency
    agency.add_property(drp1)

    # Add agent and director to agency
    agency.add_agent(agent1)
    agency.add_agent(agent2)
    agency.add_agent(agent3)
    agency.add_director(director)
    agency.add_director(director2)

    # Create properties  
    # Creat sold residential properties = Agent 1
    rp1 = Property(address="17 Nassim Road", postal_code=258390, tenure="Freehold", completion_year=1971, property_type="Residential", area=782, valuation=1096187, commission_rate=0.01)
    rp2 = Property(address="5 Caldecott Close", postal_code=299855, tenure="Commonhold", completion_year=1984, property_type="Residential", area=1163, valuation=1821789, commission_rate=0.01)
    # Creat sold residential properties = Agent 2   
    rp3 = Property(address="467 Ang Mo Kio Avenue 10", postal_code=560467, tenure="Leasehold", completion_year=2001, property_type="Residential", area=1289, valuation=2025432, commission_rate=0.01)
    rp4 = Property(address="581A Sembawang Place", postal_code=751581, tenure="Freehold", completion_year=1978, property_type="Residential", area=1345, valuation=2108109, commission_rate=0.01)
    # Creat sold residential properties = Agent 3
    rp5 = Property(address="7 Raffles Boulevard", postal_code=395956, tenure="Freehold", completion_year=1969, property_type="Residential", area=1245, valuation=1798765, commission_rate=0.01)

    # Add residencial properties to agency
    agency.add_property(rp1)
    agency.add_property(rp2)
    agency.add_property(rp3)
    agency.add_property(rp4)
    agency.add_property(rp5)

    # Add sold residential properties to agents
    agent1.add_property_sold(rp1)
    agent2.add_property_sold(rp2)
    agent3.add_property_sold(rp3)
    agent3.add_property_sold(rp4)
    agent3.add_property_sold(rp5)

    # Print properties and agents/directors
    agency.print_properties()
    agency.print_agents_directors()

if __name__ == "__main__":
    main()