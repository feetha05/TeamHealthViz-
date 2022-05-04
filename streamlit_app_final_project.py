#pip install streamlist==1.4.0
import altair as alt
import pandas as pd
import streamlit as st


# get the full data

full_df = pd.read_csv('https://raw.githubusercontent.com/feetha05/TeamHealthViz-/main/full_df.csv')

# get the pain disorder data
#pain_disorders_by_country = pd.read_csv('https://raw.githubusercontent.com/feetha05/TeamHealthViz-/main/gbd_dalys_global_trends_numbers.csv')

pain_disorders_by_country_sexes = pd.read_csv('https://raw.githubusercontent.com/feetha05/TeamHealthViz-/main/gbd_dalys_global_trends_numbers_sexes.csv')

st.sidebar.markdown('# HealthViz : Final Project')
st.sidebar.markdown('# Global Burden of Disease Data and Reporting')
st.sidebar.markdown("## Burden of Pain Related Metrics")
st.sidebar.markdown("The Global Burden of Disease (GBD) data set which provides estimates of health loss (premature death and disability) from 350 diseases and injuries in 195 countries, by age and sex, from 1990 to 2019. See more at https://ghdx.healthdata.org/gbd-results-tool")


### time seris bar chart

st.write('## Pain Disorders by Country')


chart3 = alt.Chart(pain_disorders_by_country_sexes).properties(width=100).mark_bar().encode(x=alt.X("year", title="Year"),
            y=alt.Y("val", title="DALYs (Disability-Adjusted Life Years)", sort=None),
            color=alt.Color('cause', title="Cause"),
            tooltip=[alt.Tooltip('cause', title='Cause'), 
                     alt.Tooltip('val', title='DALYs (Disability-Adjusted Life Years)')])


# Incidence of pain burden by diesase from 1990 to 2019 by subtype

st.altair_chart(chart3, use_container_width=True)


chart2 = alt.Chart(pain_disorders_by_country_sexes).mark_bar().encode(
    x='year:O',
    y='val',
    color='year:N',
    column='sex:N'
)

st.altair_chart(chart2, use_container_width=True)
#st.altair_chart(chart2, use_container_width=True)

### P1.2 ###

st.write("## Age-specific Incidence of Cause of Pain Type Across Continents")

### P2.1 ###
# replace with st.slider
#year = 2012
#subset = df[df["Year"] == year]
### P2.1 ###
st.slider('Select a Year', min_value=int(full_df["year"].min()), max_value=int(full_df["year"].max()), step=1)

### P2.2 ###
# replace with st.radio
#sex = "M"
#subset = subset[subset["Sex"] == sex]
### P2.2 ###
st.radio('Select Sex',full_df["sex"].unique())

### P2.3 ###
# replace with st.multiselect
# (hint: can use current hard-coded values below as as `default` for selector)
#subset = subset[subset["Country"].isin(countries)]
### P2.3 ###

#unique_countries = df[df['Country'].isin(countries)]

unique_locations = full_df["location"].unique()

st.multiselect('Select location',unique_locations)

### P2.4 ###
# replace with st.selectbox
#cancer = "Malignant neoplasm of stomach"
#subset = subset[subset["Cancer"] == cancer]
### P2.4 ###
st.selectbox('Select Cause of Pain',full_df["cause"].unique())
#st.selectbox('Select Cancer',df["Cancer"].unique())
### P2.5 ###
ages = ['Under 5', '5-14 years', '15-49 years',
       '50 to 74 years', '85 plus', '75 to 84']

chart = alt.Chart(full_df).mark_bar().encode(
    x=alt.X("age", sort=ages),
    y=alt.Y("val", title="Incidence"),
    color="location",
    tooltip=["val"],
).properties(
    #title=f"{cancer} mortality rates for {'males' if sex == 'M' else 'females'} in {year}",
)
### P2.5 ###

st.altair_chart(chart, use_container_width=True)

locations_in_subset = full_df["location"].unique()
if len(locations_in_subset) != len(unique_locations):
    if len(locations_in_subset) == 0:
        st.write("No data avaiable for given subset.")
    else:
        missing = set(unique_locations) - set(locations_in_subset)
        st.write("No data available for " + ", ".join(missing) + ".")