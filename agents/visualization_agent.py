import plotly.express as px

class VisualizationAgent:

    def revenue_by_product(self, df):

        product_sales = (
            df.groupby("product")["revenue"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            product_sales,
            x="product",
            y="revenue",
            title="Revenue by Product"
        )

        return fig

    def revenue_by_region(self, df):

        region_sales = (
            df.groupby("region")["revenue"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            region_sales,
            names="region",
            values="revenue",
            title="Revenue by Region"
        )

        return fig

    def revenue_trend(self, df):

        trend = (
            df.groupby("date")["revenue"]
            .sum()
            .reset_index()
        )

        fig = px.line(
            trend,
            x="date",
            y="revenue",
            title="Revenue Trend"
        )

        return fig
    
    def forecast_chart(self, forecast):

        fig = px.line(
            forecast,
            x="ds",
            y="yhat",
            title="30-Day Revenue Forecast"
        )

        return fig