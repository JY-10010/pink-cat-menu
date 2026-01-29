import streamlit as st
import random
import base64

# 1. 페이지 설정
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

# --- 세션 상태 초기화 (자동 입력을 위해 필요) ---
if 'auto_menu' not in st.session_state:
    st.session_state.auto_menu = ""

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
    .stApp {{
        background: linear-gradient(rgba(255, 240, 245, 0.5), rgba(255, 240, 245, 0.5)), 
                    url("{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
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
        height: 3rem;
        font-size: 16px;
    }}
    /* 입력창 배경 */
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.7) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

set_style('cat.png')

# 3. 앱 콘텐츠
st.markdown('<p class="main-title">🍱 러닝 후 오늘의 보상!</p>', unsafe_allow_html=True)

# 추천 메뉴 구역
st.markdown("#### 💡 이런 보상은 어때요?")
KOREAN_MENUS = ["삼겹살", "돼지갈비", "족발", "소고기", "제육볶음", "떡볶이", "치킨", "마라탕", "탕수육", "돈까스", "막창", "햄버거", "국밥", "피자", "아구찜", "백반", "생선조림", "수육", "닭도리탕", "해물탕", "회", "참치", "곱창"]
sugg = random.sample(KOREAN_MENUS, 5)
st.success(f"✨ {', '.join(sugg)}")

# 버튼 2개를 가로로 배치
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 추천 새로고침"):
        st.rerun()
with col2:
    if st.button("✅ 추천메뉴 자동적용"):
        # 추천된 5개 중 하나를 랜덤 선택해서 세션에 저장
        st.session_state.auto_menu = random.choice(sugg)
        st.rerun()

st.divider()

# 4. 입력 구역
st.markdown("#### ✨ 후보 입력 (2개 이상)")
entries = []

# 첫 번째 칸에 자동 적용 메뉴가 들어가도록 설정
first_val = st.session_state.auto_menu
entries.append(st.text_input("보상 후보 1", value=first_val, key="m_0", placeholder="자동 적용을 누르거나 직접 써주세요"))

for i in range(1, 5):
    entries.append(st.text_input(f"보상 후보 {i+1}", key=f"m_{i}", placeholder="맛있는 보상 후보"))

st.write("") 

# 5. 결과 확인
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
        # 결과 확인 후에는 자동 적용 값 초기화 (선택사항)
        st.session_state.auto_menu = ""
