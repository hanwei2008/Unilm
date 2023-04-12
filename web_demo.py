#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: web_demo.py
#Author: 韩伟
#Mail: hanwei2008123@163.com
#Created Time: 2023-04-07 01:32:57
############################

'''
CUDA_VISIBLE_DEVICES=1 streamlit run web_demo.py
'''

import streamlit as st
from streamlit_chat import message
from predict import UnilmPredictor
import json

st.set_page_config(
    page_title="NLG demo",
    page_icon="🏠"
)

st.title('文本生成模型 Demo')
st.markdown('''
## todolist
* title2job——用标题、工种、行业、薪资等生成jd
* 训练监控---仪表盘
''')
