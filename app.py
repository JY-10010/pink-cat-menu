import streamlit as st
import random
import base64

# 1. 페이지 설정
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_mobile_optimized_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    st.markdown(f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* [수정] 배경사진 위 투명도 설정 (0.5 = 50% 투명도) */
    /* 숫자가 커질수록(예: 0.8) 배경 사진이 더 하얗게 가려집니다. */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(255, 240, 245, 0.5); 
        z-index: -1;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .stTextInput>div>div>input {{
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 10px;
    }}
    .stButton>button {{
        width: 100%;
        border-radius: 25px;
        height: 3em;
        font-weight: bold;
        background-color: #FF69B4 !important;
        border: none;
    }}
    </style>
    ''', unsafe_allow_html=True)

try:
    set_mobile_optimized_bg('cat.png')
except:
    st.warning("cat.png 파일을 찾을 수 없다냥! 🐾")

# 3. [수정] 앱 콘텐츠 - 제목 크기를 80%로 조절
# font-size: 80%; 부분을 추가했습니다.
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-size: 80%;'>🍱 러닝 후 오늘의 보상!</h1>", unsafe_allow_html=True)

# 추천 메뉴 구역
st.markdown("#### 💡 이런 메뉴 어때요?")
KOREAN_MENUS = ["삼겹살", "돼지갈비", "김치찌개", "비빔밥", "제육볶음", "떡볶이", "치킨", "마라탕", "초밥", "돈가스", "짬뽕", "햄버거", "냉면", "피자"]
suggestions = random.sample(KOREAN_MENUS, 5)
st.success(" , ".join(suggestions))

if st.button("🔄 추천 새로고침"):
    st.rerun()

st.divider()

st.markdown("#### ✨ 후보 입력 (2개 이상)")
entries = []
for i in range(5):
    entries.append(st.text_input(f"후보 {i+1}", key=f"m_{i}", placeholder=f"맛있는 메뉴 {i+1}"))

st.write("") 
if st.button("🚀 니가 대신골라 줘!"):
    clean_menus = [m for m in entries if m.strip()]
    if len(clean_menus) < 2:
        st.error("후보를 2개 이상 입력해라냥! 🐾")
    else:
        selected = random.choice(clean_menus)
        st.balloons()
        st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 15px; border: 2px solid #FF69B4; text-align: center;">
                <h2 style="color: #FF69B4; margin: 0;">🎉 {selected} 🎉</h2>
            </div>
        """, unsafe_allow_html=True)
