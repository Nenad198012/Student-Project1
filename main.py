import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('The Best Company')

content = """
Flibberty gibbet, the wibberly wobbler danced on the ziggity zag.
Quixotic quarks quaffed quantum quagmires quietly.
Zizzle zazzle, the frizzle frazzle flooped in the gloopy glop.
Bingle bangle, the dingle dangle swung from the zingle zong.
Wibbly wobbly, the flibbity flabbity flopped in the zibbity zappity.
Snizzle snazzle, the frizzle frazzle flooped in the gloopy glop.
Jibber jabber, the flibber flabber flopped in the zibbity zappity.
Wizzle wazzle, the frizzle frazzle flooped in the gloopy glop.
Bingle bangle, the dingle dangle swung from the zingle zong.
"""

st.write(content)

st.header('Our Team')

col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.5, 1, 0.5, 1])
# col1, col2, col3 = st.columns([1, 1, 1])

df = pd.read_csv('data (1).csv', sep=',')

with col1:
    for index, row in df[:4].iterrows():
        full_name = row['first name'] + ' ' + row['last name']
        st.subheader(full_name.title())
        st.write(row['role'])
        st.image("images (1)/" + row['image'], use_column_width=True)

with col2:
    for index, row in df[4:8].iterrows():
        full_name = row['first name'] + ' ' + row['last name']
        st.subheader(full_name.title())
        st.write(row['role'])
        st.image("images (1)/" + row['image'], use_column_width=True)

with col3:
    for index, row in df[8:12].iterrows():
        full_name = row['first name'] + ' ' + row['last name']
        st.subheader(full_name.title())
        st.write(row['role'])
        st.image("images (1)/" + row['image'], use_column_width=True)
