from prophet import Prophet
import pandas as pd

class ForecastingAgent:

    def forecast_revenue(self, df):

        forecast_df = (
            df.groupby("date")["revenue"]
            .sum()
            .reset_index()
        )

        forecast_df.columns = ["ds", "y"]

        forecast_df["ds"] = pd.to_datetime(
            forecast_df["ds"]
        )

        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False
        )

        model.fit(forecast_df)

        future = model.make_future_dataframe(
            periods=30
        )

        forecast = model.predict(future)

        return forecast