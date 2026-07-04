import pandas as pd

from agents.cleaning_agent import CleaningAgent
from agents.analytics_agent import AnalyticsAgent

df = pd.read_csv("data/sample_sales.csv")

cleaner = CleaningAgent()

df = cleaner.clean_data(df)

analytics = AnalyticsAgent()

kpis = analytics.generate_kpis(df)

print("\n===== KPI REPORT =====\n")

for key, value in kpis.items():
    print(f"{key}: {value}")