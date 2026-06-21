import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="오늘의 체크리스트",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide standard Streamlit header/footer and pad iframe to full screen
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.block-container {
        padding: 0;
        max-width: 100%;
        height: 100vh;
    }
    iframe {
        width: 100% !important;
        height: 100vh !important;
        border: none;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 3. Read index.html content
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 4. Render HTML inside Streamlit Component
    # We set a large height (1000px) and scrolling=True to fit the design comfortably on mobile and desktop
    st.components.v1.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
