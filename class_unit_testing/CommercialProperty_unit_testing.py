from CommercialProperty import CommercialProperty

# Example commercial property
commercial_property = CommercialProperty(address="456 Commerce Blvd", postal_code="654321", tenure="Leasehold", completion_year=2015, property_type="Commercial", area=3000, valuation=1500000, commercial_type="Flatted factory")

# Calculate commission
commission = commercial_property.calculate_commission()

# Print the commercial property listing with commission
print(f"Commercial Property Listing:\n"
      f"Address: {commercial_property.address}\n"
      f"Postal Code: {commercial_property.postal_code}\n"
      f"Tenure: {commercial_property.tenure}\n"
      f"Completion Year: {commercial_property.completion_year}\n"
      f"Property Type: {commercial_property.property_type}\n"
      f"Area: {commercial_property.area} sq ft\n"
      f"Valuation: ${commercial_property.valuation}\n"
      f"Commercial Type: {commercial_property.commercial_type}\n"
      f"Commission Rate: {commercial_property.commission_rate * 100}%\n"
      f"Commission: ${commission:.2f}")
