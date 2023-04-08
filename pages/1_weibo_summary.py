import pandas as pd
import streamlit as st
from streamlit_chat import message
from predict import UnilmPredictor
import json
import time

st.set_page_config(
    page_title="weibo_title_generation",
    page_icon=":robot:"
)

st.title('微博标题生成 Demo')

@st.cache_resource
def gen_model():
    up = UnilmPredictor(model_recover_path='data/unilm_lcsts/model.3.bin')

    return up

weibo_summary_up=gen_model()

@st.cache_data
def gen_text(input_text, up=weibo_summary_up, beam_size=1):
    output_text = up.predict([{'src_text': input_text}], beam_size, need_score_traces=True)[0]

    return output_text

input_text = st.text_area(label="输入微博内容", value='''?工资日结每天270元！空调车间，工资高，环境好！上海汽配厂招缝纫工：男女不限，18-45周岁，免费工作餐，住宿每月290元！生产汽车安全气囊
电话：微信同步 班！联系电话微信同步''', height = 200, placeholder="微博正文")
beam_size = st.slider('Beam Size', 1, 8, 1)

if st.button("生成", key="predict"):
    start=time.time()
    data_info = gen_text(input_text, beam_size=beam_size)
    end=time.time()
    st.markdown('_time consumption %.3f second_'%(end-start))
    if beam_size>1:
        df_beam = pd.DataFrame(data_info['beam_seq_scores'], columns=['结果', '分数'])
        st.dataframe(df_beam)
    else:
        st.write('<p style="font-size:20px;">'+data_info['pred_text']+'</p>', unsafe_allow_html=True)
