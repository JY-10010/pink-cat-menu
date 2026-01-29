import streamlit as st
import random
import base64

# 1. 페이지 설정
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 2. 스타일 설정
def set_style(bin_file):
    try:
        bin_str = get_base64(bin_file)
        bg_img = f"data:image/png;base64,{bin_str}"
    except:
        bg_img = ""

    st.markdown(f"""
    <style>
    /* 배경 설정 (이미지에 핑크색 50% 혼합) */
    .stApp {{
        background: linear-gradient(rgba(255, 240, 245, 0.5), rgba(255, 240, 245, 0.5)), 
                    url("{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 제목 크기 (기존 대형 사이즈에서 살짝만 축소) */
    .main-title {{
        font-size: 32px !important; 
        color: #FF69B4 !important;
        text-align: center;
        font-weight: bold;
        padding: 10px 0px;
    }}

    header, footer, #MainMenu {{visibility: hidden;}}

    .stButton>button {{
        width: 100%;
        border-radius: 50px;
        background-color: #FF69B4 !important;
        color: white !important;
        border: none;
        height: 3.5rem;
        font-size: 18px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_style('cat.png')

# 3. 실제 화면 내용
st.markdown('<p class="main-title">🍱 러닝 후 오늘의 보상!</p>', unsafe_allow_html=True)

# 추천 메뉴 구역
st.markdown("#### 💡 이런 보상은 어때요?")
KOREAN_MENUS = ["삼겹살", "돼지갈비", "김치찌개", "비빔밥", "제육볶음", "떡볶이", "치킨", "마라탕", "초밥", "돈가스", "짬뽕", "햄버거", "냉면", "피자"]
sugg = random.sample(KOREAN_MENUS, 5)
st.success(f"✨ {', '.join(sugg)}")

if st.button("🔄 추천 새로고침"):
    st.rerun()

st.divider()

# 입력 구역
st.markdown("#### ✨ 후보 입력 (2개 이상)")
entries = []
for i in range(5):
    entries.append(st.text_input(f"보상 후보 {i+1}", key=f"m_{i}", placeholder="예: 아이스 아메리카노"))

st.write("") 

if st.button("🚀 니가 대신 골라 줘!"):
    clean = [m for m in entries if m.strip()]
    if len(clean) < 2:
        st.error("후보를 2개 이상 써주세요! 🐾")
    else:
        selected = random.choice(clean)
        st.balloons()
        st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 15px; border: 2px solid #FF69B4; text-align: center;">
                <h3 style="color: #FF69B4; margin: 0;">🎉 {selected} 🎉</h3>
            </div>
        """, unsafe_allow_html=True)
