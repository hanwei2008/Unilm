import pandas as pd
import streamlit as st
from streamlit_chat import message
from predict import UnilmPredictor
import json
import time

st.set_page_config(
    page_title="query2queries",
    page_icon=":robot:"
)

st.title('招工query重写生成')

@st.cache_resource
def gen_model():
    up = UnilmPredictor(model_recover_path='data/unilm_query2query_v5_user_hq/model.3.bin')

    return up

query2queries_up=gen_model()

@st.cache_data
def gen_text(input_text, up=query2queries_up, beam_size=1):
    output_text = up.predict([{'src_text': input_text}], beam_size, need_score_traces=True)[0]

    return output_text

input_query = st.text_area(label="输入query", value="大白", height = 100, placeholder="在这里输入query")
beam_size = st.slider('Beam Size', 1, 8, 4)

if st.button("生成", key="predict"):
    start=time.time()
    data_info = gen_text(input_query, beam_size=beam_size)
    end=time.time()
    st.markdown('_time consumption %.3f second_'%(end-start))
    if beam_size>1:
        df_beam = pd.DataFrame(data_info['beam_seq_scores'], columns=['结果', '分数'])
        st.dataframe(df_beam)
    else:
        st.write('<p style="font-size:20px;">'+data_info['pred_text']+'</p>', unsafe_allow_html=True)
