import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 포켓몬 테스트", page_icon="⚡", layout="centered")

# 메인 타이틀
st.title("⚡ 내 MBTI에 찰떡인 포켓몬은?")
st.write("당신의 MBTI를 선택하면, 성격과 가장 잘 어울리는 포켓몬을 추천해 드립니다!")

# MBTI별 포켓몬 데이터 (도감 번호로 고화질 공식 이미지 연동)
pokemon_data = {
    "INTJ": {"name": "뮤츠", "desc": "냉철한 전략가! 혼자만의 시간을 즐기며 엄청난 잠재력을 숨기고 있어요.", "img": "150"},
    "INTP": {"name": "후딘", "desc": "아이큐 5000의 천재! 논리적이고 분석적인 당신에게 딱 어울려요.", "img": "65"},
    "ENTJ": {"name": "리자몽", "desc": "타고난 리더! 목표를 향해 불타오르는 열정과 카리스마를 가졌네요.", "img": "6"},
    "ENTP": {"name": "팬텀", "desc": "장난기 가득한 아이디어 뱅크! 예측 불가능한 매력으로 사람들을 홀려요.", "img": "94"},
    "INFJ": {"name": "루기아", "desc": "신비로운 수호자! 깊은 통찰력으로 사람들의 마음을 꿰뚫어보고 위로해줘요.", "img": "249"},
    "INFP": {"name": "님피아", "desc": "평화주의자 요정! 따뜻한 마음씨와 뛰어난 공감 능력으로 주위를 환하게 해요.", "img": "700"},
    "ENFJ": {"name": "윈디", "desc": "정의롭고 다정한 리더! 언제나 사람들을 이끌고 챙겨주는 따뜻한 마음의 소유자예요.", "img": "59"},
    "ENFP": {"name": "이브이", "desc": "호기심 천국! 어떤 모습으로든 진화할 수 있는 무한한 가능성과 친화력을 가졌어요.", "img": "133"},
    "ISTJ": {"name": "이상해꽃", "desc": "흔들리지 않는 나무! 묵묵히 자신의 책임을 다하는 믿음직하고 차분한 성격이에요.", "img": "3"},
    "ISFJ": {"name": "럭키", "desc": "다정한 천사! 다른 사람을 챙기고 돌보는 것을 좋아하며 곁에 있으면 힘이 돼요.", "img": "113"},
    "ESTJ": {"name": "거북왕", "desc": "철저한 행동파! 강력한 물대포처럼 추진력이 넘치고 규칙과 룰을 잘 지켜요.", "img": "9"},
    "ESFJ": {"name": "푸린", "desc": "분위기 메이커! 사람들 앞에서는 걸 좋아하고 친절해서 인기가 많아요.", "img": "39"},
    "ISTP": {"name": "스라크", "desc": "쿨하고 시크한 해결사! 뛰어난 상황 판단력과 민첩한 행동력의 소유자네요.", "img": "123"},
    "ISFP": {"name": "루브도", "desc": "자유로운 영혼의 예술가! 자신만의 색깔로 세상을 아름답게 칠하고 싶어 해요.", "img": "235"},
    "ESTP": {"name": "괴력몬", "desc": "넘치는 에너지! 머리보다 몸이 먼저 반응하며 스릴과 모험을 즐기는 행동파예요.", "img": "68"},
    "ESFP": {"name": "로파파", "desc": "흥겨운 댄스 머신! 낙천적이고 언제나 파티의 중심에서 사람들을 즐겁게 해줘요.", "img": "272"}
}

st.write("---")

# MBTI 선택 드롭다운
mbti_options = ["선택하세요"] + list(pokemon_data.keys())
selected_mbti = st.selectbox("👇 당신의 MBTI를 골라주세요!", mbti_options)

# 결과 출력
if selected_mbti != "선택하세요":
    if st.button("결과 확인하기 몬스터볼 던지기! 🔴"):
        data = pokemon_data[selected_mbti]
        
        # 화면 축하 효과
        st.balloons()
        
        st.write("---")
        st.markdown(f"<h2 style='text-align: center;'>🎉 당신의 포켓몬은 <b>{data['name']}</b> 입니다!</h2>", unsafe_allow_html=True)
        
        # 포켓몬 공식 이미지 출력 (PokeAPI 활용)
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{data['img']}.png"
        
        # 이미지를 가운데 정렬하기 위해 컬럼 사용
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img_url, use_container_width=True)
        
        # 포켓몬 설명
        st.success(data['desc'])
