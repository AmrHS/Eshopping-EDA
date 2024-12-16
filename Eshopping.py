
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


Data_source= pd.read_csv('order_cust_sales_prod.csv')


Data_source.drop('Unnamed: 0', axis=1, inplace= True)
Data_source_sample = Data_source.head(10)
color1= px.colors.qualitative.Pastel

# ===========================================================
#=======
bins = [0, 19, 39, 59, 79, 99]
labels = ['0-19', '20-39', '40-59', '60-79', '80-99']
Data_source['age_range']  = pd.cut(Data_source['age'], bins=bins, labels=labels, right=True)
Data_source['age_range'].unique()

age_group = Data_source.groupby('age_range')[['total_price']].agg({
'total_price': 'sum'
}).reset_index().sort_values(by='age_range')

fig_age_group = px.pie(age_group, values='total_price', names='age_range', hole=.3,color_discrete_sequence=px.colors.qualitative.Pastel)

#========
age_avg_price = Data_source.groupby('age')[['total_price']].agg(
average_total_price =('total_price', 'mean')
).reset_index().sort_values(by='age')

fig_age_avg_price = px.line(age_avg_price, x="age", y=age_avg_price.columns[1:],color_discrete_sequence=px.colors.qualitative.Pastel)


#=========
gender_sales = Data_source.groupby('gender')[['total_price']].sum().reset_index().sort_values(by='total_price')

fig_gender_sales = px.bar(gender_sales, x='gender', y=gender_sales.columns[1:])

#============
month_sales = Data_source.groupby('month_order')[['total_price']].sum().reset_index().sort_values(by='month_order')
fig_month_sales =  px.line(month_sales, x="month_order", y=month_sales.columns[1:],color_discrete_sequence=px.colors.qualitative.Pastel)

#===========
state_sales = Data_source.groupby(['state'])[['total_price']].sum().reset_index().sort_values(by='total_price',ascending = False)
fig_state_sales = px.bar(state_sales, x='state', y=state_sales.columns[1:])

#============
state_gender_sales = Data_source.groupby(['state','gender'])[['total_price']].sum().reset_index().sort_values(by='total_price',ascending = False).head(30)
fig_state_gender_sales = px.bar(
    state_gender_sales, 
    x='total_price', 
    y='state', 
    color='gender',
    title='Total Price by State and Gender',
    text='total_price',
    orientation='h' 
)

#=============
age_per_state = Data_source.groupby(['state'])[['age']].mean().reset_index().sort_values(by='state')
fig_age_per_state = px.line(
    age_per_state,
    x='state',
    y='age',
    markers=True,
    line_shape='linear'
)

#================
age_state_per_gender = Data_source.groupby(['state','gender'])[['age']].mean().round().reset_index().sort_values(by='age',ascending = False).head(30)
fig_age_state_per_gender = px.bar(
    age_state_per_gender, 
    x='age', 
    y='state', 
    color='gender',
    text='age',
    orientation='h' 
)

#===============

product_type_sales = Data_source.groupby(['product_type'])[['total_price']].sum().reset_index().sort_values(by='total_price',ascending = False)
fig_product_type_sales =  px.pie(product_type_sales, values='total_price', names='product_type',  title='Product type sales', hole=.3,color_discrete_sequence=px.colors.qualitative.Pastel)

#==============
product_size_sales = Data_source.groupby(['size'])[['total_price']].sum().reset_index().sort_values(by='total_price',ascending = False)
fig_product_size_sales =  px.pie(product_size_sales, values='total_price', names='size',  title='Product size sales', hole=.3,color_discrete_sequence=px.colors.qualitative.Pastel)

#============================================================



# Streamlit Layout
st.title('Eshopping EDA')

# Display the sample data
st.header('Sample Data')
st.dataframe(Data_source_sample, hide_index=True)


# Display visualizations
st.header("Age group of customers")
st.plotly_chart(fig_age_group)


st.header("Age / avg purchase total")
st.plotly_chart(fig_age_avg_price)


st.header("Gender-based purchasing behaviour")
st.plotly_chart(fig_gender_sales)


st.header("What is the highest month in sales")
st.plotly_chart(fig_month_sales)


st.header("What is the highest state in sales")
st.plotly_chart(fig_state_sales)


st.header("What is the highest state per gender in sales")
st.plotly_chart(fig_state_gender_sales)


st.header("What is the average age per state")
st.plotly_chart(fig_age_per_state)

st.header("What is the average age per state per each gender")
st.plotly_chart(fig_age_state_per_gender)

st.header("What is the highest product type in sales")
st.plotly_chart(fig_product_type_sales)

st.header("What is the highest product size in sales?")
st.plotly_chart(fig_product_size_sales)
