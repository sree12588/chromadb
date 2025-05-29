import pandas as pd
import random

# Define possible values for defects
categories = ["Software", "Hardware", "UI", "Security", "Performance"]
severities = ["Critical", "High", "Medium", "Low"]
statuses = ["Open", "In Progress", "Resolved"]
descriptions = [
    "System crashes on startup",
    "Overheating issue in CPU",
    "Misalignment in dashboard layout",
    "Unauthorized access detected",
    "Slow response in data processing",
    "Memory leak in application",
    "Text formatting error in reports",
    "Hard drive failure detected",
    "SSL certificate expired",
    "Delay in network packet transmission"
    "UI elements not responsive",
    "Data corruption during transfer",
    "Inconsistent data display",
    "Error in user authentication",
    "Unexpected behavior in search function",
    "Failure to load external resources", 
    "Incorrect calculations in reports",
    "Missing error messages",
    "Inability to connect to database",
    "Failure to save user preferences",
    "Incompatibility with older versions",
    "Unexpected pop-up messages",
    "Failure to update software",
    "Incorrect data synchronization",
    "Error in file upload process",
    "Failure to generate reports",
    "Inconsistent behavior across browsers",
    "Error in payment processing",
    "Failure to send notifications",
    "Inability to access certain features",
    "Unexpected application shutdown",
    "Error in data import process",
]

# Generate 500 defect records
data = []
for i in range(1, 501):
    data.append([
        f"D{i:03}",  # Defect ID (D001, D002, ..., D500)
        random.choice(categories),
        random.choice(severities),
        random.choice(statuses),
        random.choice(descriptions)
    ])

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=["Defect_ID", "Category", "Severity", "Status", "Description"])
df.to_csv("defect_dataset.csv", index=False)
print("CSV file with 500 records saved successfully!")
