import pandas as pd
import streamlit as st
from streamlit_chat import message
import json
import time
from subprocess import run

st.set_page_config(
    page_title="模型训练监控",
    page_icon=":robot:"
)

st.title('模型监控')


cmd = st.text_area(label="输入日志查看命令", value='tail -c 3000 data/log_train_job2title.txt', height = 50, placeholder="日志查看命令")


if st.button("运行", key="run"):
    cmd_result = run(cmd, shell=True, capture_output=True, text=True)
    if cmd_result.stdout:
        st.info(cmd_result.stdout)
    if cmd_result.stderr:
        st.error(cmd_result.stderr)
