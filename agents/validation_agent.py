class ValidationAgent:

    REQUIRED_COLUMNS = [
        "date",
        "product",
        "region",
        "units_sold",
        "revenue",
        "profit"
    ]

    def validate(self, df):

        columns = [c.lower().strip() for c in df.columns]

        missing = []

        for col in self.REQUIRED_COLUMNS:
            if col not in columns:
                missing.append(col)

        if missing:
            return False, missing

        return True, []