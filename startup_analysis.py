# ===============================
# STARTUP ECOSYSTEM ANALYSIS
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta


class StartupAnalyzer:
    """
    Class to generate, analyze, and visualize startup data
    """

    def __init__(self, records=1000):
        self.records = records
        self.data = None

    # ------------------------------
    # DATASET GENERATION
    # ------------------------------
    def generate_dataset(self):

        industries = ["FinTech","HealthTech","EdTech","AI","Ecommerce",
                      "SaaS","AgriTech","CleanTech","CyberSecurity"]

        locations = ["Bangalore","Mumbai","Delhi NCR","Hyderabad","Chennai",
                     "Pune","San Francisco","New York","London","Berlin"]

        funding_rounds = ["Seed","Series A","Series B","Series C","Series D"]

        investors = ["Sequoia","Accel","Tiger Global","Softbank",
                     "Lightspeed","Benchmark","Matrix","Y Combinator"]

        start_date = datetime(2020,1,1)
        end_date = datetime(2023,12,31)

        dataset = []

        for i in range(self.records):

            random_days = random.randint(0,(end_date-start_date).days)

            record = {
                "date": start_date + timedelta(days=random_days),
                "company_name": f"Startup_{i}",
                "industry": random.choice(industries),
                "location": random.choice(locations),
                "funding_round": random.choice(funding_rounds),
                "amount_raised": round(np.random.uniform(500000,150000000),2),
                "lead_investor": random.choice(investors),
                "co_investors": random.randint(0,10),
                "valuation": round(np.random.uniform(5000000,1000000000),2)
            }

            dataset.append(record)

        self.data = pd.DataFrame(dataset)

        print("\nDataset Created Successfully")
        print(self.data.head())

    # ------------------------------
    # DATA CLEANING
    # ------------------------------
    def clean_data(self):
        try:
            self.data["date"] = pd.to_datetime(self.data["date"])

            # Fill missing values
            self.data.fillna(self.data.median(numeric_only=True), inplace=True)

            # Remove invalid values
            self.data = self.data[self.data["amount_raised"] > 0]

            print("\nData Cleaned Successfully")

        except Exception as e:
            print("Error:", e)

    # ------------------------------
    # BASIC METRICS
    # ------------------------------
    def basic_metrics(self):

        print("\nBASIC METRICS")

        print("Total Funding:", self.data["amount_raised"].sum())
        print("Unique Companies:", self.data["company_name"].nunique())
        print("Average Deal Size:", self.data["amount_raised"].mean())
        print("Total Deals:", len(self.data))

    # ------------------------------
    # FUNDING TRENDS
    # ------------------------------
    def funding_trends(self):

        self.data["year"] = self.data["date"].dt.year
        self.data["month"] = self.data["date"].dt.month

        yearly = self.data.groupby("year")["amount_raised"].sum()

        print("\nYearly Funding:")
        print(yearly)

    # ------------------------------
    # INDUSTRY ANALYSIS
    # ------------------------------
    def industry_analysis(self):

        print("\nIndustry Analysis:")

        industry = self.data.groupby("industry").agg({
            "amount_raised":["sum","mean","count"]
        })

        print(industry)

    # ------------------------------
    # GEOGRAPHIC ANALYSIS
    # ------------------------------
    def geographic_analysis(self):

        print("\nGeographic Analysis:")

        location = self.data.groupby("location").agg({
            "amount_raised":["sum","mean","count"]
        })

        print(location)

    # ------------------------------
    # INVESTOR ANALYSIS
    # ------------------------------
    def investor_analysis(self):

        print("\nTop Investors:")

        investors = self.data["lead_investor"].value_counts()
        print(investors)

    # ------------------------------
    # VISUALIZATIONS
    # ------------------------------
    def visualizations(self):

        sns.set()

        # 1. Funding Trend
        yearly = self.data.groupby(self.data["date"].dt.year)["amount_raised"].sum()

        plt.figure()
        yearly.plot(marker="o")
        plt.title("Funding Trend")
        plt.show()

        # 2. Industry Pie
        industry = self.data.groupby("industry")["amount_raised"].sum()

        plt.figure()
        plt.pie(industry, labels=industry.index, autopct="%1.1f%%")
        plt.title("Industry Distribution")
        plt.show()

        # 3. Location Bar
        location = self.data.groupby("location")["amount_raised"].sum()

        plt.figure()
        location.sort_values().plot(kind="barh")
        plt.title("Funding by Location")
        plt.show()

        # 4. Funding Stage
        stage = self.data.groupby("funding_round")["amount_raised"].mean()

        plt.figure()
        stage.plot(kind="bar")
        plt.title("Funding Stage Analysis")
        plt.show()

        # 5. Investor Activity
        investors = self.data["lead_investor"].value_counts()

        plt.figure()
        sns.barplot(x=investors.values, y=investors.index)
        plt.title("Top Investors")
        plt.show()

        # 6. Custom Insight
        plt.figure()
        sns.scatterplot(
            x="amount_raised",
            y="valuation",
            hue="funding_round",
            data=self.data
        )
        plt.title("Valuation vs Funding")
        plt.show()


# ===============================
# MAIN EXECUTION
# ===============================

if __name__ == "__main__":

    analyzer = StartupAnalyzer(1200)

    analyzer.generate_dataset()
    analyzer.clean_data()

    analyzer.basic_metrics()
    analyzer.funding_trends()
    analyzer.industry_analysis()
    analyzer.geographic_analysis()
    analyzer.investor_analysis()

    analyzer.visualizations()
