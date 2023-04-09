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


cmd = st.text_area(label="输入日志查看命令", value='tail -n1 data/log_train_job2title.txt', height = 50, placeholder="日志查看命令")
logtxtbox = st.empty()

col1, col2, col3 = st.columns([3,3,8])
is_start = col1.button("开始查看", key="run")
is_stop = col2.button("停止查看", key="stop")
if is_start:
    #pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    while True:
        output = subprocess.getoutput(cmd)
        logtxtbox.info(output)
        if is_stop:
            break
        else:
            time.sleep(0.1)

