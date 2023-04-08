import streamlit as st
from streamlit_chat import message
from predict import UnilmPredictor
import json
import time

st.set_page_config(
    page_title="job2queries",
    page_icon=":robot:"
)

st.title('根据招工详情生成query')

@st.cache_resource
def gen_model():
    up = UnilmPredictor(model_recover_path='data/unilm_job2queries/model.1.bin')

    return up

up=gen_model()

@st.cache_data
def gen_text(input_text, up=up):
    output_text = up.predict([{'src_text': input_text}])[0]

    return output_text

input_query = st.text_area(label="输入招工详情", value='''招聘
                           菜鸟招聘普工20人,工价最低20元/小时。
                                                     工作内容:快递分拣,包装,扫描,发运,合单,上下架等
                                                     工作要求:18**40周岁,识字,会写字,沟通流利,配合加班;男工优先
                                                     工作时间:800**20:00左右,长
                                                     白班工作
                                                     待遇:底薪+加班+岗位津贴+绩效
                                                     (月综合5200元**6500元左
                                                     右);
提供餐补贴10元
晋升空间：操作工**小组长**班长;转正后可交五险一金。
联系电话：''', height = 300, placeholder="招工详情")

if st.button("生成", key="predict"):
    start=time.time()
    data_info = gen_text(input_query)
    end=time.time()
    st.markdown('_time consumption %.3f second_'%(end-start))
    st.write('<p style="font-size:20px;">'+data_info['pred_text']+'</p>', unsafe_allow_html=True)
