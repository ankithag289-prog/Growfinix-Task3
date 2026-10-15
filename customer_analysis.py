import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output folder
os.makedirs("output", exist_ok=True)

# Load dataset
df = pd.read_csv("tourism.csv")
df.columns = df.columns.str.strip()

print("GROWFINIX TASK 3: CUSTOMER DEMOGRAPHIC ANALYSIS")
print("=" * 50)

# Dataset overview
print("Total records:", len(df))
print("\nColumn names:")
print(df.columns.tolist())

# Clean numeric columns
for col in ["Age", "MonthlyIncome", "NumberOfTrips"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate records
df = df.drop_duplicates()
print("Records after removing duplicates:", len(df))

# 1. Customer travel behaviour
# This dataset has NumberOfTrips, not Destination.
if "NumberOfTrips" in df.columns:
    trips = df["NumberOfTrips"].dropna()
    trip_counts = trips.value_counts().sort_index()

    print("\nCustomers by number of trips:")
    print(trip_counts)

    trip_counts.to_csv("output/travel_trips.csv")

    if not trip_counts.empty:
        plt.figure(figsize=(8, 5))
        trip_counts.plot(kind="bar", edgecolor="black")
        plt.title("Customer Travel Behaviour")
        plt.xlabel("Number of Trips")
        plt.ylabel("Number of Customers")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig("output/travel_trips.png")
        plt.close()

# 2. Customer age distribution
if "Age" in df.columns:
    ages = df["Age"].dropna()

    if not ages.empty:
        plt.figure(figsize=(8, 5))
        plt.hist(ages, bins=15, edgecolor="black")
        plt.title("Customer Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Number of Customers")
        plt.tight_layout()
        plt.savefig("output/age_distribution.png")
        plt.close()

        age_groups = pd.cut(
            ages,
            bins=[0, 25, 35, 45, 55, float("inf")],
            labels=["18-25", "26-35", "36-45", "46-55", "56+"]
        )

        print("\nCustomers by age group:")
        print(age_groups.value_counts().sort_index())

        age_groups.value_counts().sort_index().to_csv(
            "output/age_groups.csv"
        )

# 3. Customer income distribution
if "MonthlyIncome" in df.columns:
    income = df["MonthlyIncome"].dropna()

    if not income.empty:
        plt.figure(figsize=(8, 5))
        plt.hist(income, bins=15, edgecolor="black")
        plt.title("Customer Monthly Income Distribution")
        plt.xlabel("Monthly Income")
        plt.ylabel("Number of Customers")
        plt.tight_layout()
        plt.savefig("output/income_distribution.png")
        plt.close()

        income_groups = pd.cut(
            income,
            bins=[
                -float("inf"), 25000, 50000,
                100000, float("inf")
            ],
            labels=[
                "Below 25,000",
                "25,000-50,000",
                "50,000-100,000",
                "Above 100,000"
            ]
        )

        print("\nCustomers by income group:")
        print(income_groups.value_counts().sort_index())

        income_groups.value_counts().sort_index().to_csv(
            "output/income_groups.csv"
        )

# 4. Missing-value report
print("\nMissing values in each column:")
print(df.isnull().sum())

df.isnull().sum().to_csv("output/missing_values.csv")

print("\nAnalysis completed successfully!")
print("Charts and reports are saved in the output folder.")