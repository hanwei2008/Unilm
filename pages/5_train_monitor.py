import os
import signal
import pandas as pd
import streamlit as st
from streamlit_chat import message
import json
import time
from subprocess import run
import subprocess

st.set_page_config(
    page_title="模型训练监控",
    page_icon=":robot:"
)

st.title('模型监控')


cmd = st.text_area(label="输入日志查看命令", value='tail -c100 data/log_train_job2title.txt', height = 50, placeholder="日志查看命令")

col1, col2, col3 = st.columns([3,3,8])
bt = col1.empty()
is_start = bt.button("开始查看", key="run")
logtxtbox = st.empty()
if is_start:
    is_stop = bt.button("停止查看", key="stop")
    while True:
        if is_stop:
            is_start = bt.button("开始查看", key="run_1")
            break
        output = subprocess.getoutput(cmd)
        logtxtbox.info(output)
        time.sleep(0.1)
