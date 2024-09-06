from Property import Property

# Example property
property = Property(address="123 Main St", postal_code="123456", tenure="Freehold", completion_year=2010, property_type="Residential", area=1200, valuation=1000000)
# Calculate commission
commission = property.calculate_commission()
# Print the property listing with commission
print(f"Property Listing:\n"
      f"Address: {property.address}\n"
      f"Postal Code: {property.postal_code}\n"
      f"Tenure: {property.tenure}\n"
      f"Completion Year: {property.completion_year}\n"
      f"Property Type: {property.property_type}\n"
      f"Area: {property.area} sq ft\n"
      f"Valuation: ${property.valuation}\n"
      f"Commission Rate: {property.commission_rate * 100}%\n"
      f"Commission: ${commission:.2f}")
