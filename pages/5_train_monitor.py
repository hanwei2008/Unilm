import os
import signal
import pandas as pd
import streamlit as st
from streamlit_chat import message
import json
import time
from subprocess import run
import subprocess
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from utils.system_monitor import pcInfo

st.set_page_config(
    page_title="模型训练监控",
    page_icon=":robot:"
)

# 权限管理
with open('conf/config.yaml', 'r') as fr:
    config = yaml.load(fr, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

st.title('训练监控')

if authentication_status:
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
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout:
                logtxtbox.info(result.stdout)
            if result.stderr:
                logtxtbox.stderr(result.stderr)
            time.sleep(0.1)
    # 系统资源监控

    st.markdown('## CPU信息(G)：')
    df_tmp = pd.DataFrame([pcInfo.GetCpuInfo()], columns='核数，线程数，CPU使用率'.split('，'))
    st.write(df_tmp.to_html(index=False), unsafe_allow_html=True)

    st.markdown('## GPU信息(G)：')
    df_tmp = pd.DataFrame(pcInfo.GetGpuInfo(), columns='GPU序号，GPU总量，GPU使用量，gpu使用占比'.split('，'))
    st.write(df_tmp.to_html(index=False), unsafe_allow_html=True)

    st.markdown('## 内存信息(G)：')
    df_tmp = pd.DataFrame([pcInfo.GetMemoryInfo()], columns='总内存，已用内存，空闲内存，内存使用率'.split('，'))
    st.write(df_tmp.to_html(index=False), unsafe_allow_html=True)

    st.markdown('## 硬盘信息(G)：')
    df_tmp = pd.DataFrame(pcInfo.GetDiskInfo(), columns='序号，磁盘名称，总大，已用大小，剩余大小，占用率'.split('，'))
    st.write(df_tmp.to_html(index=False), unsafe_allow_html=True)

    st.markdown('## CPU温度：')
    st.json(pcInfo.GetCPUTmpInfo())
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
