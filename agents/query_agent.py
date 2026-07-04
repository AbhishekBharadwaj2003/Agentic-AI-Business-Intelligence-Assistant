from services.llm_service import LLMService


class QueryAgent:

    def __init__(self):

        self.llm = LLMService()

    def ask_question(self, question, kpis, summary):

        prompt = f"""
You are an experienced Business Intelligence Consultant.

Provide concise, data-driven business insights.
Always explain your reasoning using the provided KPIs.
When appropriate, suggest practical recommendations to improve business performance.
Never make up information that is not present in the provided data.

Below are the business insights generated from the uploaded dataset.

Business KPIs

Total Revenue:
{kpis["Total Revenue"]}

Total Profit:
{kpis["Total Profit"]}

Profit Margin:
{kpis["Profit Margin %"]}%

Top Product:
{kpis["Top Product"]}

Top Region:
{kpis["Top Region"]}

Executive Summary

{summary}

User Question

{question}

Instructions:

- Answer only using the information above.
- Keep the answer professional.
- Give business recommendations whenever appropriate.
- Limit the answer to around 150 words.
"""

        answer = self.llm.ask_llm(prompt)

        return answer