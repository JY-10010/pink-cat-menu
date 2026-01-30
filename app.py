import streamlit as st
import random
import base64

# 1. 페이지 설정
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

# --- 전체 메뉴 데이터베이스 (추천 리스트 외에도 여기서 랜덤 추출) ---
KOREAN_MENUS_DB = [
    "삼겹살", "돼지갈비", "족발", "소고기", "제육볶음", "떡볶이", "치킨", "마라탕", 
    "탕수육", "돈까스", "막창", "햄버거", "국밥", "피자", "아구찜", "백반", 
    "생선조림", "수육", "닭도리탕", "해물탕", "회", "참치", "곱창", "샤브샤브", 
    "냉면", "칼국수", "초밥", "스테이크", "파스타", "양꼬치"
]

# --- 세션 상태 초기화 ---
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = random.sample(KOREAN_MENUS_DB, 5)

if 'input_values' not in st.session_state:
    st.session_state.input_values = [""] * 5

# --- 버튼 클릭 이벤트 함수 ---

# [수정] 한 번에 5개 칸을 전체 DB에서 랜덤하게 채움
def apply_all_menus():
    # 전체 메뉴 리스트에서 중복 없이 5개를 뽑아 한꺼번에 기입
    st.session_state.input_values = random.sample(KOREAN_MENUS_DB, 5)

def refresh_suggestions():
    st.session_state.suggestions = random.sample(KOREAN_MENUS_DB, 5)
    st.session_state.input_values = [""] * 5 # 새로고침 시 모든 칸 비움

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
        height: 3.5rem;
        font-size: 14px;
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
st.markdown("#### 💡 이런 보상은 어때요?")
st.success(f"✨ {', '.join(st.session_state.suggestions)}")

col1, col2 = st.columns(2)
with col1:
    st.button("🔄 추천 새로고침", on_click=refresh_suggestions)
with col2:
    # [수정] 텍스트 변경
    st.button("✅ 5칸 한꺼번에 채우기", on_click=apply_all_menus)

st.divider()

# 4. 입력 구역
st.markdown("#### ✨ 후보 입력 (직접 수정 가능)")
entries = []

for i in range(5):
    val = st.session_state.input_values[i]
    # 사용
