import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("marketing_funnel.xlsx")

# -----------------------------
# Overall Funnel Metrics
# -----------------------------
total_visitors = df['Visitors'].sum()
total_leads = df['Leads'].sum()
total_customers = df['Customers'].sum()

visitor_to_lead = (total_leads / total_visitors) * 100
lead_to_customer = (total_customers / total_leads) * 100
overall_conversion = (total_customers / total_visitors) * 100

print("===== OVERALL FUNNEL ANALYSIS =====")
print(f"Total Visitors: {total_visitors}")
print(f"Total Leads: {total_leads}")
print(f"Total Customers: {total_customers}")
print(f"Visitor → Lead Conversion Rate: {visitor_to_lead:.2f}%")
print(f"Lead → Customer Conversion Rate: {lead_to_customer:.2f}%")
print(f"Overall Conversion Rate: {overall_conversion:.2f}%")

# -----------------------------
# Drop-Off Analysis
# -----------------------------
visitor_dropoff = total_visitors - total_leads
lead_dropoff = total_leads - total_customers

print("\n===== DROP-OFF ANALYSIS =====")
print(f"Visitors Lost Before Becoming Leads: {visitor_dropoff}")
print(f"Leads Lost Before Becoming Customers: {lead_dropoff}")

# -----------------------------
# Channel Performance
# -----------------------------
channel_analysis = df.groupby('Channel').agg({
    'Visitors': 'sum',
    'Leads': 'sum',
    'Customers': 'sum'
})

channel_analysis['Visitor_to_Lead_%'] = (
    channel_analysis['Leads'] /
    channel_analysis['Visitors'] * 100
)

channel_analysis['Lead_to_Customer_%'] = (
    channel_analysis['Customers'] /
    channel_analysis['Leads'] * 100
)

print("\n===== CHANNEL PERFORMANCE =====")
print(channel_analysis)

# -----------------------------
# Funnel Chart
# -----------------------------
stages = ['Visitors', 'Leads', 'Customers']
values = [total_visitors, total_leads, total_customers]

#plt.figure(figsize=(8,5))
#plt.bar(stages, values)
#plt.title("Marketing Funnel")
#plt.ylabel("Count")
#plt.show()

# -----------------------------
# Channel-wise Customers
# -----------------------------
#channel_analysis['Customers'].plot(
    #kind='bar',
    #figsize=(8,5),
    #title='Customers by Channel'
#)

#plt.ylabel('Customers')
#plt.show()

# -----------------------------
# Monthly Trend Analysis
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])

monthly = df.groupby(df['Date'].dt.to_period('M')).agg({
    'Visitors':'sum',
    'Leads':'sum',
    'Customers':'sum'
})

monthly.index = monthly.index.astype(str)

#monthly.plot(figsize=(10,6))
#plt.title("Monthly Funnel Trends")
#plt.ylabel("Count")
#plt.show()

# -----------------------------
# Best Performing Channel
# -----------------------------
best_channel = channel_analysis['Lead_to_Customer_%'].idxmax()

print("\n===== INSIGHTS =====")
print(f"Best Quality Lead Source: {best_channel}")
print("Channel with highest Lead → Customer conversion rate.")
print(f"Best Quality Lead Source: {best_channel}")
# ==========================
# DASHBOARD (4 SECTIONS)
# ==========================

visitor_dropoff_rate = ((total_visitors - total_leads) / total_visitors) * 100
lead_dropoff_rate = ((total_leads - total_customers) / total_leads) * 100

conversion_rates = {
    'Visitor→Lead': visitor_to_lead,
    'Lead→Customer': lead_to_customer,
    'Overall': overall_conversion
}
# Dashboard Title
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle(
    "Marketing & Lead Funnel Analysis Dashboard",
    fontsize=18,
    fontweight='bold'
)

# 1. Funnel Analysis (Bar Chart)
axes[0, 0].bar(
    ['Visitors', 'Leads', 'Customers'],
    [total_visitors, total_leads, total_customers]
)
axes[0, 0].set_title('Funnel Overview')

# 2. High-Quality Leads by Channel (Pie Chart)
axes[0, 1].pie(
    channel_analysis['Customers'],
    labels=channel_analysis.index,
    autopct='%1.1f%%'
)
axes[0, 1].set_title('Customer Distribution by Channel')

# 3. Conversion Rates (Horizontal Bar Chart)
conversion_labels = ['Visitor→Lead', 'Lead→Customer', 'Overall']
conversion_values = [
    visitor_to_lead,
    lead_to_customer,
    overall_conversion
]

axes[1, 0].barh(
    conversion_labels,
    conversion_values
)
axes[1, 0].set_title('Conversion Rates (%)')

# 4. Drop-off Rates (Line Chart)
visitor_dropoff_rate = (
    (total_visitors - total_leads) / total_visitors
) * 100

lead_dropoff_rate = (
    (total_leads - total_customers) / total_leads
) * 100

axes[1, 1].plot(
    ['Visitor→Lead', 'Lead→Customer'],
    [visitor_dropoff_rate, lead_dropoff_rate],
    marker='o'
)
axes[1, 1].set_title('Drop-off Rates (%)')

plt.tight_layout()
plt.show()
