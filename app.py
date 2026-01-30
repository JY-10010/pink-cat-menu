import streamlit as st
import random
import base64

# 1. 페이지 설정
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

# --- 전체 메뉴 데이터베이스 ---
KOREAN_MENUS_DB = [
    "삼겹살", "돼지갈비", "족발", "소고기", "제육볶음", "떡볶이", "치킨", "마라탕", 
    "탕수육", "돈까스", "막창", "햄버거", "국밥", "피자", "아구찜", "백반", 
    "생선조림", "수육", "닭도리탕", "해물탕", "회", "참치", "곱창", "샤브샤브", 
    "냉면", "칼국수", "초밥", "스테이크", "파스타", "양꼬치"
]

# --- 세션 상태 초기화 (입력값 고정) ---
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = random.sample(KOREAN_MENUS_DB, 5)

# 입력창 5개의 값을 개별적으로 관리
for i in range(5):
    if f'menu_input_{i}' not in st.session_state:
        st.session_state[f'menu_input_{i}'] = ""

# --- 버튼 클릭 함수 ---
def apply_all_menus():
    # 전체 DB에서 랜덤하게 5개를 뽑아 각 세션에 저장
    random_picks = random.sample(KOREAN_MENUS_DB, 5)
    for i in range(5):
        st.session_state[f'menu_input_{i}'] = random_picks[i]

def refresh_suggestions():
    st.session_state.suggestions = random.sample(KOREAN_MENUS_DB, 5)
    # 입력창 모두 비우기
    for i in range(5):
        st.session_state[f'menu_input_{i}'] = ""

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# 2. 스타일 설정
def set_style(bin_file):
    bg_img_data = get_base64(bin_file)
    bg_style = f'url("data:image/png;base64,{bg_img_data}")' if bg_img_data else "none"

    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 240, 245, 0.5), rgba(255, 240, 245, 0.5)), {bg_style};
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
        height: 3.5rem;
        font-weight: bold;
    }}
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.7) !important;
        border-radius: 10px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

set_style('cat.png')

# 3. 앱 콘텐츠
st.markdown('<p class="main-title">🍱 러닝 후 오늘의 보상!</p>', unsafe_allow_html=True)

# 추천 메뉴 구역
st.markdown("#### 💡 이런 보상은 어때요?")
st.success(f"✨ {', '.join(st.session_state.suggestions)}")

col1, col2 = st.columns(2)
with col1:
    st.button("🔄 추천 새로고침", on_click=refresh_suggestions)
with col2:
    st.button("✅ 5칸 한꺼번에 채우기", on_click=apply_all_menus)

st.divider()

# 4. 입력 구역 (안정적인 세션 연동 방식)
st.markdown("#### ✨ 후보 입력 (직접 수정 가능)")
entries = []

for i in range(5):
    # 각 입력창을 세션 값과 직접 연결 (value=st.session_state[...])
    user_input = st.text_input(
        f"보상 후보 {i+1}", 
        value=st.session_state[f'menu_input_{i}'], 
        key=f"widget_input_{i}"
    )
    # 사용자가 직접 입력한 내용을 즉시 세션에 저장
    st.session_state[f'menu_input_{i}'] = user_input
    entries.append(user_input)

st.write("") 

# 5. 결과 확인
if st.button("🚀 니가 대신 골라 줘!"):
    clean = [m for m in entries if m.strip()]
    if len(clean) < 2:
        st.error("후보를 2개 이상 채워달라냥! 🐾")
    else:
        selected = random.choice(clean)
        st.balloons()
        st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 15px; border: 2px solid #FF69B4; text-align: center;">
                <h3 style="color: #FF69B4; margin: 0;">🎉 {selected} 🎉</h3>
            </div>
        """, unsafe_allow_html=True)
