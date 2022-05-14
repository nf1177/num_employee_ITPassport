import pandas as pd

import altair as alt
import streamlit as st
import datetime

data_num_employee = pd.read_csv("num_employee.csv")


st.title('受講者数可視化')

st.sidebar.write("""## 表示年度選択""")
s_year, e_year = st.sidebar.slider(
    '範囲を指定してください。',
    2010, 2022, (2010, 2022)
)
domain_pd = pd.to_datetime(
    [str(s_year)+'-01-01', str(e_year)+'-01-01']).astype(int) / 10 ** 6


num_employee = st.multiselect(
    '企業規模を選択してください。',
    list(data_num_employee["従業員数"].unique().tolist()),
    ["50人未満"]
)

class_shiken = st.selectbox(
    '見たい受講区分を選択してください。',
    list(data_num_employee["区分"].unique()))

st.write(class_shiken)
st.write(type(class_shiken))
data = data_num_employee[data_num_employee["従業員数"].isin(num_employee)]
data = data[data['区分'] == class_shiken]


chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8, clip=True)
    .encode(
        x=alt.X("年度:T",
                scale=alt.Scale(domain=list(domain_pd))),
        y=alt.Y("人数:Q", stack=None),
        color='従業員数:N'
    )
)
st.altair_chart(chart, use_container_width=True)
