class SummaryAgent:

    def generate_summary(self, kpis):

        summary = f"""
Executive Summary

• Total Revenue : ₹{kpis['Total Revenue']:,.0f}

• Total Profit : ₹{kpis['Total Profit']:,.0f}

• Profit Margin : {kpis['Profit Margin %']}%

• Best Performing Product :
{kpis['Top Product']}

• Highest Revenue Region :
{kpis['Top Region']}

Business Recommendation

Increase investment in the best-performing product and focus marketing efforts in the highest revenue region.
"""

        return summary