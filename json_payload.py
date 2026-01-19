def validate_funds_transfer(data):
    required_fields = [
        "Posting.Amount",
        "Posting.DebitAccount",
        "Posting.CreditAccount",
        "Institution.InstitutionCode"
    ]

    for field in required_fields:
        keys = field.split(".")
        value = data
        for key in keys:
            value = value.get(key, {})
        if not value or (isinstance(value, str) and value.strip() == ""):
            return f"❌ Missing or empty required field: {field}"
    return "✅ All required fields are present."

# Sample input structure
sample_data = {
    "Posting": {
        "Amount": "3552.5",
        "DebitAccount": "4299349922625556",
        "CreditAccount": ""  # Intentionally missing for testing
    },
    "Institution": {
        "InstitutionCode": "4299349922"
    }
}
# Validate the sample data
result = validate_funds_transfer(sample_data)
print(result)  # Output: ❌ Missing or empty required field: Posting.CreditAccount
