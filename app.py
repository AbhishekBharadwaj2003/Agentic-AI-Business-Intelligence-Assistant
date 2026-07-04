import streamlit as st
import pandas as pd

from agents.validation_agent import ValidationAgent
from agents.cleaning_agent import CleaningAgent
from agents.analytics_agent import AnalyticsAgent
from agents.visualization_agent import VisualizationAgent
from agents.forecasting_agent import ForecastingAgent
from agents.summary_agent import SummaryAgent
from agents.report_agent import ReportAgent
from agents.query_agent import QueryAgent

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Agentic AI Business Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

div[data-testid="metric-container"]{
    background:white;
    border:1px solid #E5E7EB;
    padding:18px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.title("📊 Agentic AI Business Intelligence Assistant")

st.info(
    "AI-Powered Business Intelligence Dashboard | "
    "Data Cleaning • KPI Analysis • Visualization • Forecasting • Reporting"
)

st.markdown("""
Upload a business dataset and automatically perform:

- ✅ Data Validation
- ✅ Data Cleaning
- ✅ KPI Generation
- ✅ Interactive Visualization
- ✅ Revenue Forecasting
- ✅ Executive Summary
- ✅ PDF Report Generation
""")

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("⚙️ Control Panel")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    st.success("System Ready")

    st.divider()

# ==========================================================
# CACHE
# ==========================================================

@st.cache_data
def load_data(file):

    return pd.read_csv(file)

# ==========================================================
# WAIT FOR FILE
# ==========================================================

if uploaded_file is None:

    st.info("📂 Please upload a CSV file.")

    st.stop()

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data(uploaded_file)

st.success("✅ Dataset Uploaded Successfully!")

# ==========================================================
# VALIDATION
# ==========================================================

validator = ValidationAgent()

valid, missing = validator.validate(df)

if not valid:

    st.error(
        f"Missing Columns : {', '.join(missing)}"
    )

    st.stop()

# ==========================================================
# CLEANING
# ==========================================================

cleaner = CleaningAgent()

df = cleaner.clean_data(df)

# ==========================================================
# ANALYTICS
# ==========================================================

analytics = AnalyticsAgent()

kpis = analytics.generate_kpis(df)

# ==========================================================
# SUMMARY
# ==========================================================

summary_agent = SummaryAgent()

summary = summary_agent.generate_summary(kpis)

# ==========================================================
# VISUALIZATION
# ==========================================================

viz = VisualizationAgent()

# ==========================================================
# REPORT
# ==========================================================

report_agent = ReportAgent()

# ==========================================================
# SESSION STATE
# ==========================================================

if "ai_answer" not in st.session_state:
    st.session_state.ai_answer = ""

if "user_question" not in st.session_state:
    st.session_state.user_question = ""

# ==========================================================
# SIDEBAR AI ASSISTANT
# ==========================================================

with st.sidebar:

    st.subheader("🤖 AI Business Assistant")

    question = st.text_input(
        "Ask your business question",
        value=st.session_state.user_question,
        placeholder="Example: Why is my profit low?"
    )

    if st.button(
        "Ask AI",
        use_container_width=True
    ):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            try:

                with st.spinner("Analyzing business data..."):

                    query_agent = QueryAgent()

                    response = query_agent.ask_question(
                        question,
                        kpis,
                        summary
                    )

                    st.write(response)

                    st.session_state.ai_answer = response
                    st.session_state.user_question = question

                st.success("Analysis Complete")

            except Exception as e:

                st.error(str(e))

    st.divider()

    st.caption("© 2026 Abhishek Bharadwaj")

# ==========================================================
# CREATE TABS
# ==========================================================

dashboard_tab, forecast_tab, report_tab, about_tab = st.tabs(
    [
        "📊 Dashboard",
        "📈 Forecast",
        "📄 Report",
        "ℹ️ About"
    ]
)

# ==========================================================
# DASHBOARD TAB
# ==========================================================

with dashboard_tab:

    st.header("Business Dashboard")

    st.write(
        "A complete overview of your uploaded business dataset."
    )

    st.divider()

    # ======================================================
    # KPI CARDS
    # ======================================================

    st.subheader("Key Performance Indicators")

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    with kpi1:

        st.metric(
            "Revenue",
            f"₹{kpis['Total Revenue']:,.0f}"
        )

    with kpi2:

        st.metric(
            "Profit",
            f"₹{kpis['Total Profit']:,.0f}"
        )

    with kpi3:

        st.metric(
            "Margin",
            f"{kpis['Profit Margin %']}%"
        )

    with kpi4:

        st.metric(
            "Top Product",
            kpis["Top Product"]
        )

    with kpi5:

        st.metric(
            "Top Region",
            kpis["Top Region"]
        )

    st.divider()

    # ======================================================
    # DATASET OVERVIEW
    # ======================================================

    st.subheader("Dataset Overview")

    d1, d2, d3, d4 = st.columns(4)

    with d1:

        st.metric(
            "Rows",
            len(df)
        )

    with d2:

        st.metric(
            "Columns",
            len(df.columns)
        )

    with d3:

        st.metric(
            "Products",
            df["product"].nunique()
        )

    with d4:

        st.metric(
            "Regions",
            df["region"].nunique()
        )

    st.divider()

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    st.subheader("Executive Summary")

    st.success(summary)

    st.divider()

    # ======================================================
    # AI BUSINESS ASSISTANT RESPONSE
    # ======================================================

    st.subheader("🤖 AI Business Assistant")

    if st.session_state.ai_answer:

        st.success(st.session_state.ai_answer)

    else:

        st.info(
            "Ask a question from the sidebar to receive AI-powered business insights."
        )

    st.divider()

    # ======================================================
    # BUSINESS CHARTS
    # ======================================================

    st.subheader("Business Insights")

    chart_left, chart_right = st.columns(2)

    with chart_left:

        st.plotly_chart(
            viz.revenue_trend(df),
            use_container_width=True
        )

    with chart_right:

        st.plotly_chart(
            viz.revenue_by_product(df),
            use_container_width=True
        )

    st.divider()

    # ======================================================
    # SECOND ROW
    # ======================================================

    table_col, pie_col = st.columns([2, 1])

    with table_col:

        st.subheader("Top Products")

        st.dataframe(
            analytics.top_products(df),
            use_container_width=True,
            hide_index=True
        )

    with pie_col:

        st.plotly_chart(
            viz.revenue_by_region(df),
            use_container_width=True
        )

# ==========================================================
# FORECAST TAB
# ==========================================================

with forecast_tab:

    st.header("Revenue Forecast")

    st.write(
        """
Forecast future revenue using Facebook Prophet.

The forecasting model learns historical sales patterns
and predicts the revenue for the next 30 days.
"""
    )

    st.divider()

    if st.button(
        "Generate Revenue Forecast",
        use_container_width=True,
        key="forecast_button"
    ):

        with st.spinner("Training Forecast Model..."):

            forecast_agent = ForecastingAgent()

            forecast = forecast_agent.forecast_revenue(df)

        st.success("✅ Forecast Generated Successfully")

        st.plotly_chart(
            viz.forecast_chart(forecast),
            use_container_width=True
        )

        st.info(
            """
This forecast is generated using Facebook Prophet,
which is widely used for business time-series forecasting.
"""
        )

# ==========================================================
# REPORT TAB
# ==========================================================

with report_tab:

    st.header("Business Report")

    st.write(
        """
Generate a professional business report and export your
processed dataset.
"""
    )

    st.divider()

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    st.subheader("Executive Summary")

    st.success(summary)

    st.divider()

    # ======================================================
    # CLEANED DATASET
    # ======================================================

    st.subheader("Cleaned Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ======================================================
    # DOWNLOAD CLEANED CSV
    # ======================================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # PDF REPORT
    # ======================================================

    st.subheader("PDF Business Report")

    st.write(
        """
Generate a PDF report containing:

- Business KPIs
- Executive Summary
- Business Recommendations
"""
    )

    if st.button(
        "📄 Generate PDF Report",
        use_container_width=True,
        key="pdf_button"
    ):

        with st.spinner("Generating PDF Report..."):

            pdf_path = report_agent.generate_report(
                kpis,
                summary
            )

        st.success("✅ PDF Report Generated Successfully")

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf,
                file_name="Business_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

# ==========================================================
# ABOUT TAB
# ==========================================================

with about_tab:

    st.header("ℹ️ About This Project")

    st.write("""
The **Agentic AI Business Intelligence Assistant** is a
resume-quality Business Intelligence application built using
Python and Streamlit.

The application automates business data analysis through
modular agents that validate, clean, analyze, visualize,
forecast and summarize business datasets.
""")

    st.divider()

    # ======================================================
    # PROJECT WORKFLOW
    # ======================================================

    st.subheader("Project Workflow")

    st.code(
"""
                Upload CSV
                     │
                     ▼
          Validation Agent
                     │
                     ▼
           Cleaning Agent
                     │
                     ▼
          Analytics Agent
                     │
                     ▼
       Visualization Agent
                     │
                     ▼
        Forecasting Agent
                     │
                     ▼
      Executive Summary Agent
                     │
                     ▼
          Report Generation
                     │
                     ▼
        AI Business Assistant
""",
        language="text"
    )

    st.divider()

    # ======================================================
    # TECH STACK
    # ======================================================

    st.subheader("Tech Stack")

    left, right = st.columns(2)

    with left:

        st.markdown("""
### Backend

- Python
- Pandas
- Prophet
- ReportLab
- Groq API
- Llama 3
""")

    with right:

        st.markdown("""
### Frontend

- Streamlit
- Plotly
- Custom CSS
- Modular Agent Architecture
""")

    st.divider()

    # ======================================================
    # PROJECT MODULES
    # ======================================================

    st.subheader("Project Modules")

    st.markdown("""
- ✅ Validation Agent
- ✅ Cleaning Agent
- ✅ Analytics Agent
- ✅ Visualization Agent
- ✅ Forecasting Agent
- ✅ Executive Summary Agent
- ✅ Report Generation Agent
- ✅ AI Query Agent
- ✅ LLM Service

Each module follows the **Single Responsibility Principle (SRP)**,
making the application modular, reusable and easy to maintain.
""")

    st.divider()

    # ======================================================
    # FEATURES
    # ======================================================

    st.subheader("Features")

    f1, f2 = st.columns(2)

    with f1:

        st.markdown("""
### Analytics

- CSV Upload
- Data Validation
- Data Cleaning
- KPI Generation
- Executive Summary
- Interactive Charts
""")

    with f2:

        st.markdown("""
### Intelligence

- Revenue Forecasting
- AI Business Assistant
- Business Recommendations
- PDF Report
- CSV Export
""")

    st.divider()

    # ======================================================
    # DEVELOPER
    # ======================================================

    st.subheader("👨‍💻 Developer")

    st.info("""
**Abhishek Bharadwaj**

B.Tech - Electronics and Communication Engineering

VIT-AP University

**Career Interests**

- Data Analytics
- Business Intelligence
- Data Science
- Artificial Intelligence
- Machine Learning
""")
    
# ==========================================================
# FOOTER
# ==========================================================

st.divider()

footer_left, footer_center, footer_right = st.columns([2, 3, 2])

with footer_left:

    st.caption("Agentic AI Business Intelligence Assistant")

with footer_center:

    st.caption(
        " "
    )

with footer_right:

    st.caption("© 2026 Abhishek Bharadwaj")