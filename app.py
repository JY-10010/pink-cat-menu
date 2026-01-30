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

# --- 세션 상태 초기화 ---
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = random.sample(KOREAN_MENUS_DB, 5)

if 'input_values' not in st.session_state:
    st.session_state.input_values = [""] * 5

# 버튼 클릭 시 입력창을 강제로 새로 그리기 위한 버전 번호
if 'version' not in st.session_state:
    st.session_state.version = 0

# --- 버튼 클릭 함수 ---
def apply_all_menus():
    # 전체 메뉴에서 5개 추출
    st.session_state.input_values = random.sample(KOREAN_MENUS_DB, 5)
    # 버전 번호를 올려서 입력창 key를 변경 (강제 새로고침 효과)
    st.session_state.version += 1

def refresh_suggestions():
    st.session_state.suggestions = random.sample(KOREAN_MENUS_DB, 5)
    st.session_state.input_values = [""] * 5
    st.session_state.version += 1

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# 2. 스타일 설정
def set_style(bin_file):
    bg_data = get_base64(bin_file)
    bg_style = f'url("data:image/png;base64,{bg_data}")' if bg_data else "none"
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 240, 245, 0.5), rgba(255, 240, 245, 0.5)), {bg_style};
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .main-title {{
        font-size: 32px !important; color: #FF69B4 !important;
        text-align: center; font-weight: bold; padding: 10px 0px;
    }}
    header, footer, #MainMenu {{visibility: hidden;}}
    .stButton>button {{
        width: 100%; border-radius: 50px; background-color: #FF69B4 !important;
        color: white !important; border: none; height: 3rem; font-weight: bold;
    }}
    .stTextInput input {{ background-color: rgba(255, 255, 255, 0.7) !important; border-radius: 10px !important; }}
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
    st.button("✅ 5칸 한꺼번에 채우기", on_click=apply_all_menus)

st.divider()

# 4. 입력 구역 (버전 번호를 활용한 강제 업데이트)
st.markdown("#### ✨ 후보 입력 (직접 수정 가능)")
final_entries = []

for i in range(5):
    # key에 st.session_state.version을 포함시켜 버튼 클릭 시 입력창을 새로 만듦
    val = st.session_state.input_values[i]
    user_input = st.text_input(
        f"보상 후보 {i+1}", 
        value=val, 
        key=f"input_v{st.session_state.version}_{i}"
    )
    final_entries.append(user_input)

st.write("") 

# 5. 결과 확인
if st.button("🚀 니가 대신 골라 줘!"):
    clean = [m for m in final_entries if m.strip()]
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
