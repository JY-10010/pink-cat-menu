import streamlit as st
import random
import base64

# 1. 페이지 설정 (브라우저 탭 제목)
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

# 배경 이미지를 위한 인코딩 함수
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 배경 스타일 설정 함수
def set_mobile_optimized_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    st.markdown(f'''
    <style>
    /* 1. 앱 전체 배경색 설정 (사진 뒤에 깔리는 색상) */
    .stApp {{
        background-color: #FFF0F5; /* 연핑크색 */
    }}

    /* 2. 배경 이미지 자체에 투명도(opacity) 적용 */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        
        /* 사진 설정 */
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;          /* 화면에 꽉 채움 */
        background-position: center;     /* 중앙 정렬 */
        background-repeat: no-repeat;
        background-attachment: fixed;    /* 스크롤 시 고정 */
        
        /* [핵심] 투명도 설정: 0.1(매우 투명) ~ 1.0(원래 선명도) */
        /* 0.5는 50%의 선명도를 의미합니다. */
        opacity: 0.5; 
        
        z-index: -1;
    }}

    /* 상단 메뉴 및 푸터 숨기기 (앱처럼 보이게) */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* 입력창 디자인 (반투명 하얀색) */
    .stTextInput>div>div>input {{
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 10px;
    }}
    
    /* 버튼 디자인 (핑크색) */
    .stButton>button {{
        width: 100%;
        border-radius: 25px;
        height: 3em;
        font-weight: bold;
        background-color: #FF69B4 !important;
        color: white !important;
        border: none;
    }}
    </style>
    ''', unsafe_allow_html=True)

# 사진 적용 (파일명이 cat.png인지 확인하세요)
try:
    set_mobile_optimized_bg('cat.png')
except:
    st.warning("cat.png 파일을 찾을 수 없다냥! 🐾")

# 3. 앱 콘텐츠 영역
# [수정] font-size: 80% 적용하여 제목 크기 축소
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-size: 180%;'>🍱 러닝 후 오늘의 보상!</h1>", unsafe_allow_html=True)

# 추천 메뉴 구역
st.markdown("#### 💡 이런 메뉴 어때요?")
KORE
