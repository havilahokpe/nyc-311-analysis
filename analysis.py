import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sodapy import Socrata
import os
from dotenv import load_dotenv

load_dotenv()
print("NYC 311 Analysis Project")

client = Socrata("data.cityofnewyork.us", os.getenv("SOCRATA_APP_TOKEN"))

results = client.get(
    "erm2-nwe9",
    limit=1000
)

df = pd.DataFrame.from_records(results)

print(df.head())
print(df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nTop 10 Complaint Types:")
print(df["complaint_type"].value_counts().head(10).to_string())
top_complaints = df["complaint_type"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_complaints.plot(kind="bar")
plt.title("Top 10 NYC 311 Complaint Types")
plt.xlabel("Complaint Type")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()



# Complaints by Borough
borough_counts = df["borough"].value_counts()

print("\nComplaints by Borough:")
print(borough_counts)

plt.figure(figsize=(10, 6))
borough_counts.plot(kind="bar")
plt.tight_layout()
plt.savefig("complaints_by_borough.png")
plt.show()
plt.title("NYC 311 Complaints by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()
# Complaints Over Time
df["created_date"] = pd.to_datetime(df["created_date"])

daily_counts = df.groupby(df["created_date"].dt.date).size()

print("\nComplaints Over Time:")
print(daily_counts)

plt.figure(figsize=(10, 6))
daily_counts.plot(kind="line", marker="o")
plt.savefig("complaints_over_time.png")

plt.title("NYC 311 Complaints Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Complaints")

plt.tight_layout()
plt.show()
