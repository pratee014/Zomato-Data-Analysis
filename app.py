import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Page configuration
st.set_page_config(page_title="Zomato Analysis", page_icon="🍴", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        color: white;
        
    }
    
    .step-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        margin-top: 2rem;
        color: black !important;
    }
    .step-container p{
          color: black !important;  }      
    h1 {
        color: #e23744 !important;
        text-align: center;
        padding: 1rem 0;
    }
    h2 {
        color: #2c3e50 !important;
        border-bottom: 3px solid #e23744;
        padding-bottom: 0.5rem;
    }
    .insight-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        color: black !important;
    }
    .insight-box p{
         color: black !important;   
        }   
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        color: black !important;
    }
    .metric-card p{
          color:Black !important;
      }
    p, div, span, label {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.markdown("<h1>🍴 Zomato Data Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 1.2rem;'>Explore restaurant trends, ratings, and customer preferences</p>", unsafe_allow_html=True)

st.markdown("---")

# ------------------------
# Step 1: Load dataset
# ------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Zomato-data-.csv", encoding="latin-1")
    return df

df = load_data()

st.markdown("""
<div class='step-container'>
    <h2>📊 Step 1: Dataset Overview</h2>
    <p><b>Understanding the Data:</b> This dataset contains information about restaurants listed on Zomato, including their names, 
    locations, cuisines, ratings, and cost. We'll analyze this data to uncover insights about restaurant trends and customer preferences. 
    Let's start by exploring the first few records to understand the structure of our data.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='metric-card'>
        <h4>Total Restaurants</h4>
        <p >{:,}</p>
    </div>
    """.format(len(df)), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <h4>Total Columns</h4>
        <p>{}</p>
    </div>
    """.format(len(df.columns)), unsafe_allow_html=True)


st.subheader("")
st.dataframe(df.head(10), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 2: Data Cleaning
# ------------------------
st.markdown("""
<div class='step-container'>
    <h2>🧹 Step 2: Data Cleaning and Preparation</h2>
    <p><b>Cleaning the Ratings:</b> The rating column contains values in the format "4.1/5". 
    We need to extract just the numerical rating (4.1) to perform mathematical operations. 
    This cleaning step converts the rating from text format to a decimal number, 
    making it ready for analysis and visualization.</p>
</div>
""", unsafe_allow_html=True)

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

df['rate'] = df['rate'].apply(handleRate)

col1, col2 = st.columns(2)
with col1:
    st.subheader("✅ Cleaned Ratings Sample")
    st.dataframe(df[['name', 'rate']].head(10), use_container_width=True)
    
with col2:
    st.subheader("🔍 Missing Values Check")
    missing_values = df.isnull().sum()
    missing_df = pd.DataFrame({
        'Column': missing_values.index,
        'Missing Count': missing_values.values,
        'Percentage': (missing_values.values / len(df) * 100).round(2)
    })
    st.dataframe(missing_df[missing_df['Missing Count'] > 0], use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 3: Restaurant Types Analysis
# ------------------------

st.markdown("""
<div class='step-container'>
    <h2>🏪 Step 3: Restaurant Types Analysis</h2>
<p><b>Categorizing Restaurants:</b> Zomato categorizes restaurants into different types like Dining, Cafes, Delivery, etc. 
Understanding the distribution of restaurant types helps us identify which categories are most popular on the platform. 
This analysis reveals market saturation and opportunities in different restaurant segments.</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribution of Restaurant Types")
    fig, ax = plt.subplots(figsize=(10, 6))
    type_counts = df['listed_in(type)'].value_counts()
    colors = sns.color_palette("husl", len(type_counts))
    ax.bar(type_counts.index, type_counts.values, color=colors)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Restaurant Type', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
    plt.title('Count of Restaurants by Type', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.markdown(f"""
        <div class='insight-box'>
            <p><b>💡 Insight:</b> The most common restaurant type is <b>{type_counts.index[0]}</b> with <b>{type_counts.values[0]:,}</b> restaurants, indicating strong demand in this category.</p>
        </div>
    """, unsafe_allow_html=True)


with col2:
    st.subheader("Total Votes by Restaurant Type")
    grouped_data = df.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(grouped_data.index, grouped_data.values, c='#e23744', marker='o', linewidth=3, markersize=10)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Restaurant Type', fontsize=12, fontweight='bold')
    plt.ylabel('Total Votes', fontsize=12, fontweight='bold')
    plt.title('Customer Engagement by Restaurant Type', fontsize=14, fontweight='bold', pad=20)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.markdown(f"""
        <div class='insight-box'>
            <p><b>💡 Insight:</b> <b>{grouped_data.index[0]}</b> restaurants received the most votes (<b>{grouped_data.values[0]:,}</b>), showing highest customer engagement and popularity.</p>
        </div>
        """, unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 4: Most Voted Restaurant
# ------------------------
st.markdown("""<div class='step-container'>
             <h2>🏆 Step 4: Most Popular Restaurant</h2>
<p><b>Finding the Champion:</b> Votes represent customer engagement and popularity. The restaurant with the maximum votes 
indicates strong customer satisfaction and brand loyalty. This metric helps identify market leaders and successful 
business models that others can learn from.</p>
""", unsafe_allow_html=True)

max_votes = df['votes'].max()
restaurant_with_max_votes = df.loc[df['votes'] == max_votes]

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f"""
<div style='
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 1.5rem 2rem;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 1rem;
'>
    <h2 style='color: white; margin: 0;'>&#x1F947; {restaurant_with_max_votes['name'].values[0]}</h2>
    <h1 style='color: white; margin: 0.2rem 0;'>{max_votes:,} Votes</h1>
    <p style='font-size: 1.1rem; margin: 0;'>&#x2B50; Rating: {restaurant_with_max_votes['rate'].values[0]}/5</p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 5: Online Order Analysis
# ------------------------

st.markdown("""<div class='step-container'>
             <h2>🛵 Step 5: Online Order Availability</h2>
<p><b>Digital Presence:</b> In today's digital age, online ordering capability is crucial for restaurant success. 
This analysis shows how many restaurants offer online ordering versus those that don't. It reflects the digital 
transformation in the food industry and customer convenience preferences.</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    fig, ax = plt.subplots(figsize=(8, 6))
    online_counts = df['online_order'].value_counts()
    colors = ['#4CAF50', '#FF5252']
    wedges, texts, autotexts = ax.pie(online_counts.values, labels=online_counts.index, autopct='%1.1f%%', 
                                        colors=colors, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax.set_title('Online Order Availability', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x=df['online_order'], palette=['#4CAF50', '#FF5252'], ax=ax)
    ax.set_xlabel('Online Order Available', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
    ax.set_title('Restaurant Count by Online Order Availability', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

online_pct = (online_counts['Yes'] / online_counts.sum() * 100).round(1)

st.markdown(f"""
<div class='insight-box'>
    <p><b>💡 Insight:</b> <b>{online_pct}%</b> of restaurants offer online ordering, showing significant digital adoption in the food service industry.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 6: Ratings Distribution
# ------------------------
st.markdown("""<div class='step-container'>
            <h2>⭐ Step 6: Ratings Distribution Analysis</h2>
<p><b>Quality Assessment:</b> Restaurant ratings reflect customer satisfaction and food quality. By analyzing the distribution 
of ratings, we can understand overall service quality standards in the market. A normal distribution centered around 3.5-4.0 
indicates consistent quality across most restaurants.<p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(12, 6))
    n, bins, patches = plt.hist(df['rate'], bins=20, color='#667eea', edgecolor='black', alpha=0.7)
    
    # Color gradient
    cm = plt.cm.RdYlGn
    for i, patch in enumerate(patches):
        patch.set_facecolor(cm(i / len(patches)))
    
    plt.xlabel('Rating', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
    plt.title('Distribution of Restaurant Ratings', fontsize=14, fontweight='bold', pad=20)
    plt.axvline(df['rate'].mean(), color='red', linestyle='--', linewidth=2, label=f'Average: {df["rate"].mean():.2f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.metric("Average Rating", f"{df['rate'].mean():.2f} ⭐")
    st.metric("Highest Rating", f"{df['rate'].max():.1f} ⭐")
    st.metric("Lowest Rating", f"{df['rate'].min():.1f} ⭐")
    st.metric("Median Rating", f"{df['rate'].median():.2f} ⭐")

average_rating = df['rate'].mean()

st.markdown(f"""
<div class='insight-box'>
    <p><b>💡 Insight:</b> Most restaurants cluster around the <b>{average_rating:.2f}</b> rating mark, indicating consistent service quality. Very few restaurants fall below 2.5 or above 4.5.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 7: Cost Analysis
# ------------------------
st.markdown("""<div class='step-container'>
            <h2>💰 Step 7: Cost Analysis for Couples</h2>
<p><b>Pricing Strategy:</b> Understanding the cost distribution helps identify price positioning and market segments. 
This analysis shows the approximate cost for two people dining, revealing affordability patterns and helping customers 
find restaurants within their budget while helping businesses position their pricing competitively.<p>
""", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(14, 6))
cost_counts = df['approx_cost(for two people)'].value_counts().sort_index()
top_costs = cost_counts.nlargest(20)
colors = plt.cm.viridis(np.linspace(0, 1, len(top_costs)))
ax.bar(range(len(top_costs)), top_costs.values, color=colors)
ax.set_xticks(range(len(top_costs)))
ax.set_xticklabels(top_costs.index, rotation=45, ha='right')
plt.xlabel('Approximate Cost for Two People', fontsize=12, fontweight='bold')
plt.ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
plt.title('Top 20 Most Common Price Points', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
st.pyplot(fig)
plt.close()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Average Cost", f"₹{df['approx_cost(for two people)'].mean():.0f}")
with col2:
    st.metric("Median Cost", f"₹{df['approx_cost(for two people)'].median():.0f}")
with col3:
    st.metric("Max Cost", f"₹{df['approx_cost(for two people)'].max():.0f}")
with col4:
    st.metric("Min Cost", f"₹{df['approx_cost(for two people)'].min():.0f}")

median_cost = df['approx_cost(for two people)'].median()

st.markdown(f"""
<div class='insight-box'>
    <p><b>💡 Insight:</b> Most restaurants are positioned in the mid-range segment with median cost around <b>₹{median_cost:.0f}</b> for two people, making dining affordable for most customers.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 8: Online vs Offline Ratings
# ------------------------
st.markdown("""<div class='step-container'>
            <h2>📱 Step 8: Online vs Offline Order Ratings Comparison</h2>
<p><b>Service Quality Comparison:</b> This boxplot compares ratings between restaurants that offer online ordering versus 
those that don't. The visualization helps us understand if digital presence correlates with better customer satisfaction. 
The median line inside each box shows the typical rating, while the box boundaries show the range where most ratings fall.</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(10, 7))
    bp = sns.boxplot(x='online_order', y='rate', data=df, palette=['#4CAF50', '#FF5252'], ax=ax)
    ax.set_xlabel('Online Order Available', fontsize=12, fontweight='bold')
    ax.set_ylabel('Rating', fontsize=12, fontweight='bold')
    ax.set_title('Rating Distribution: Online vs Offline Orders', fontsize=14, fontweight='bold', pad=20)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    online_avg = df[df['online_order'] == 'Yes']['rate'].mean()
    offline_avg = df[df['online_order'] == 'No']['rate'].mean()
    
    st.metric("Online Order Avg Rating", f"{online_avg:.2f} ⭐")
    st.metric("Offline Order Avg Rating", f"{offline_avg:.2f} ⭐")
    
    difference = abs(online_avg - offline_avg)
    better = "Online" if online_avg > offline_avg else "Offline"
    st.metric("Rating Difference", f"{difference:.2f}", delta=f"{better} is better")
if online_avg > offline_avg:
    insight_text = f"Restaurants with online ordering have <b>{difference:.2f}</b> points higher average rating, suggesting that digital convenience positively impacts customer satisfaction."
else:
    insight_text = f"Restaurants without online ordering have <b>{difference:.2f}</b> points higher average rating, indicating that traditional dine-in focused establishments maintain strong quality standards."

st.markdown(f"""
<div class='insight-box'>
    <p><b>💡 Insight:</b> {insight_text}</p>
</div>
""", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Step 9: Heatmap Analysis
# ------------------------

st.markdown("""<div class='step-container'>
            <h2>🔥 Step 9: Restaurant Type vs Online Order Heatmap</h2>
<p><b>Digital Adoption Patterns:</b> This heatmap reveals which types of restaurants have embraced online ordering and which 
haven't. Darker colors indicate higher numbers. This correlation analysis helps identify which restaurant categories 
are leading in digital transformation and which segments have opportunities for growth in online services.</p>
""", unsafe_allow_html=True)

pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, cmap='YlOrRd', fmt='d', ax=ax, cbar_kws={'label': 'Number of Restaurants'},
            linewidths=0.5, linecolor='gray')
plt.title('Restaurant Type vs Online Order Availability', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Online Order Available', fontsize=12, fontweight='bold')
plt.ylabel('Restaurant Type', fontsize=12, fontweight='bold')
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Calculate percentages
pivot_pct = pivot_table.div(pivot_table.sum(axis=1), axis=0) * 100

col1, col2 = st.columns(2)
with col1:
    st.subheader("Online Order Adoption Rate by Type")
    adoption_df = pd.DataFrame({
        'Restaurant Type': pivot_pct.index,
        'Online %': pivot_pct['Yes'].round(1)
    }).sort_values('Online %', ascending=False)
    st.dataframe(adoption_df, use_container_width=True)

with col2:
    most_digital = pivot_pct['Yes'].idxmax()
    most_digital_pct = pivot_pct['Yes'].max()
    least_digital = pivot_pct['Yes'].idxmin()
    least_digital_pct = pivot_pct['Yes'].min()
    
    
st.markdown(f"""
<div class='insight-box'>
    <p><b>💡 Key Insights:</b></p>
    <ul style='margin-top: 5px; padding-left: 1.2rem;'>
        <li><b>{most_digital}</b> leads in digital adoption with <b>{most_digital_pct:.1f}%</b> offering online orders</li>
        <li><b>{least_digital}</b> has the lowest adoption at <b>{least_digital_pct:.1f}%</b></li>
        <li>Clear opportunity for growth in traditional dining segments</li>
    </ul>
</div>
""", unsafe_allow_html=True)




st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# Final Summary
# ------------------------
st.markdown(f"""
<div class='step-container'>
    <h2>📈 Summary and Key Takeaways</h2>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎯 Business Insights
    - The restaurant landscape is dominated by dining establishments
    - Digital adoption is strong but varies by restaurant type
    - Average ratings suggest consistent quality standards
    - Mid-range pricing dominates the market
    """)

with col2:
    st.markdown("""
    ### 💡 Recommendations
    - Restaurants should consider online ordering for better reach
    - Focus on maintaining ratings above 3.5 for competitiveness
    - Price positioning around median attracts most customers
    - Customer engagement (votes) correlates with success
    """)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit | Data Source: Zomato</p>", unsafe_allow_html=True)