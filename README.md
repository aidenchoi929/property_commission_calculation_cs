# property_commission_calculation_cs
A property commission calculator by python through object-oriented-programming(OOP)
  - A program calculates property sale commission based on the position(Agent or Director)
  - Run "main.py" for overview commission slip

Commission breakdown for agenct and director
  1. Property: 1% of the property valuation(sold price) will be arranged as commission and shared into two shares(Agent and agency).
  2. Director: Directors can make earnings from commission sharing and overriding fee.
    o Commission sharing: 75~90% of commission
      ▪ Condition 1: If the director sells a property(Director becomes the agent)
      ▪ Condition 2: Rate varies based on each director’s commission sharing rate(Default rate is 75%, up to 90%)
    o Overriding fee: 5~15% of agent’s commission sharing
      ▪ Condition 1: Director receives overriding fee when the agent under supervision closes a deal.
      ▪ Condition 2: The overriding fee is calculated based on the agent’s commission sharing but it is deducted from agency’s commission sharing, and the rate varies based on director’s overriding fee rate.
  3. Agent: Agent only makes earning from the properties on he/she sells.
     -Commission sharing: 70% of commission(Fixed)

