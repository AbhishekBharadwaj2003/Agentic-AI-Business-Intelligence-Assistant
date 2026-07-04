class AnalyticsAgent:

    def generate_kpis(self, df):

        total_revenue = df["revenue"].sum()

        total_profit = df["profit"].sum()

        avg_revenue = df["revenue"].mean()

        profit_margin = (total_profit / total_revenue) * 100

        top_product = (
            df.groupby("product")["revenue"]
            .sum()
            .idxmax()
        )

        top_region = (
            df.groupby("region")["revenue"]
            .sum()
            .idxmax()
        )

        return {
            "Total Revenue": round(total_revenue, 2),
            "Total Profit": round(total_profit, 2),
            "Average Revenue": round(avg_revenue, 2),
            "Profit Margin %": round(profit_margin, 2),
            "Top Product": top_product,
            "Top Region": top_region
        }

    def top_products(self, df):

        return (
            df.groupby("product")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )