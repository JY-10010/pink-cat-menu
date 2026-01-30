import streamlit as st
import random
import base64

# 1. 페이지 설정
st.set_page_config(page_title="러닝 후 오늘의 보상!", layout="centered")

# --- 세션 상태 초기화 (데이터 유지 및 자동 입력을 위해) ---
if 'suggestions' not in st.session_state:
    KOREAN_MENUS = ["삼겹살", "돼지갈비", "족발", "소고기", "제육볶음", "떡볶이", "치킨", "마라탕", "탕수육", "돈까스", "막창", "햄버거", "국밥", "피자", "아구찜", "백반", "생선조림", "수육", "닭도리탕", "해물탕", "회", "참치", "곱창"]
    st.session_state.suggestions = random.sample(KOREAN_MENUS, 5)

if 'auto_menu' not in st.session_state:
    st.session_state.auto_menu = ""

# --- 버튼 클릭 이벤트 함수 ---
def apply_menu():
    # 현재 추천 리스트 중 하나를 랜덤으로 선택하여 저장
    st.session_state.auto_menu = random.choice(st.session_state.suggestions)

def refresh_suggestions():
    # 메뉴 리스트를 새로 뽑고 자동 적용 칸도 비움
    KOREAN_MENUS = ["삼겹살", "돼지갈비", "족발", "소고기", "제육볶음", "떡볶이", "치킨", "마라탕", "탕수육", "돈까스", "막창", "햄버거", "국밥", "피자", "아구찜", "백반", "생선조림", "수육", "닭도리탕", "해물탕", "회", "참치", "곱창"]
    st.session_state.suggestions = random.sample(KOREAN_MENUS, 5)
    st.session_state.auto_menu = ""

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 2. 스타일 설정 (배경 및 모바일 최적화)
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

# 추천 메뉴 박스
st.markdown("#### 💡 이런 보상은 어때요?")
st.success(f"✨ {', '.join(st.session_state.suggestions)}")

# 가로 버튼 배치
col1, col2 = st.columns(2)
with col1:
    st.button("🔄 추천 새로고침", on_click=refresh_suggestions)
with col2:
    st.button("✅ 추천메뉴 자동적용", on_click=apply_menu)

st.divider()

# 4. 입력 구역
st.markdown("#### ✨ 후보 입력 (2개 이상)")
entries = []

# [핵심 수정] key 값에 auto_menu를 포함하여 버튼 클릭 시 입력창을 강제 렌더링함
entries.append(st.text_input("보상 후보 1", value=st.session_state.auto_menu, key=f"m_0_{st.session_state.auto_menu}"))

for i in range(1, 5):
    entries.append(st.text_input(f"보상 후보 {i+1}", key=f"m_{i}"))

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
