import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="🎯",
    layout="centered"
)

pokemon_by_mbti = {
    "INTJ": {
        "name": "뮤츠",
        "type": "에스퍼",
        "reason": "전략적이고 독립적이며 강한 통찰력을 가진 INTJ의 이미지와 잘 어울립니다.",
        "style": "장기적인 계획을 세우고 혼자서도 강하게 성장하는 타입"
    },
    "INTP": {
        "name": "후딘",
        "type": "에스퍼",
        "reason": "호기심이 많고 분석적인 INTP의 특징이 높은 지능의 포켓몬과 잘 맞습니다.",
        "style": "깊이 생각하고 지식을 탐구하는 타입"
    },
    "ENTJ": {
        "name": "리자몽",
        "type": "불꽃 / 비행",
        "reason": "카리스마 있고 주도적인 ENTJ의 에너지와 강렬한 존재감이 닮아 있습니다.",
        "style": "팀을 이끌고 목표를 향해 직진하는 타입"
    },
    "ENTP": {
        "name": "팬텀",
        "type": "고스트 / 독",
        "reason": "재치 있고 발상이 독특한 ENTP의 장난기와 창의성이 잘 드러납니다.",
        "style": "새로운 아이디어를 던지고 분위기를 뒤흔드는 타입"
    },
    "INFJ": {
        "name": "루기아",
        "type": "에스퍼 / 비행",
        "reason": "조용하지만 깊이 있고 상징적인 INFJ의 분위기와 신비로운 이미지가 어울립니다.",
        "style": "겉으로는 차분하지만 내면의 신념이 강한 타입"
    },
    "INFP": {
        "name": "이브이",
        "type": "노말",
        "reason": "가능성이 많고 감수성이 풍부한 INFP의 모습이 여러 진화 가능성을 지닌 이브이와 잘 맞습니다.",
        "style": "자신만의 길을 찾으며 성장하는 타입"
    },
    "ENFJ": {
        "name": "픽시",
        "type": "페어리",
        "reason": "따뜻하고 사람들을 돌보는 ENFJ의 성향이 포근한 매력의 포켓몬과 어울립니다.",
        "style": "주변 사람을 챙기고 긍정적 분위기를 만드는 타입"
    },
    "ENFP": {
        "name": "피카츄",
        "type": "전기",
        "reason": "밝고 활발하며 사랑받는 ENFP의 매력이 대표적인 포켓몬 이미지와 잘 연결됩니다.",
        "style": "에너지가 넘치고 어디서든 존재감이 큰 타입"
    },
    "ISTJ": {
        "name": "거북왕",
        "type": "물",
        "reason": "책임감 있고 신뢰할 수 있는 ISTJ의 성격이 안정감 있는 포켓몬과 잘 맞습니다.",
        "style": "묵묵하게 자기 역할을 끝까지 해내는 타입"
    },
    "ISFJ": {
        "name": "해피너스",
        "type": "노말",
        "reason": "배려심 깊고 헌신적인 ISFJ의 성향이 치유와 돌봄의 이미지와 잘 어울립니다.",
        "style": "조용히 주변을 보살피는 타입"
    },
    "ESTJ": {
        "name": "보스로라",
        "type": "강철 / 바위",
        "reason": "체계적이고 실용적인 ESTJ의 단단함과 추진력이 인상적으로 닮아 있습니다.",
        "style": "질서와 책임을 중시하며 중심을 잡는 타입"
    },
    "ESFJ": {
        "name": "윈디",
        "type": "불꽃",
        "reason": "사교적이고 따뜻한 ESFJ의 성향이 믿음직하고 친근한 이미지와 어울립니다.",
        "style": "사람들과 잘 어울리고 분위기를 안정시키는 타입"
    },
    "ISTP": {
        "name": "루카리오",
        "type": "격투 / 강철",
        "reason": "실용적이고 냉정하면서도 뛰어난 감각을 지닌 ISTP의 이미지와 잘 맞습니다.",
        "style": "말보다 실력으로 보여주는 타입"
    },
    "ISFP": {
        "name": "나인테일",
        "type": "불꽃",
        "reason": "섬세하고 감각적인 ISFP의 분위기가 아름답고 우아한 포켓몬과 잘 어울립니다.",
        "style": "조용하지만 자신만의 감성을 지닌 타입"
    },
    "ESTP": {
        "name": "초염몽",
        "type": "격투",
        "reason": "즉흥적이고 대담한 ESTP의 행동력이 강렬한 액션형 포켓몬 이미지와 맞닿아 있습니다.",
        "style": "현장에서 빠르게 판단하고 움직이는 타입"
    },
    "ESFP": {
        "name": "푸린",
        "type": "노말 / 페어리",
        "reason": "사람들과 즐겁게 어울리고 분위기를 밝히는 ESFP의 매력이 잘 드러납니다.",
        "style": "재미와 친밀함으로 모두를 끌어당기는 타입"
    }
}

mbti_list = list(pokemon_by_mbti.keys())

st.title("🎯 MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면, 어울리는 포켓몬을 추천해드립니다.")

selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    mbti_list,
    index=None,
    placeholder="예: INFJ"
)

if selected_mbti:
    result = pokemon_by_mbti[selected_mbti]

    st.subheader(f"{selected_mbti}에게 어울리는 포켓몬은...")
    st.success(f"✨ {result['name']} 입니다!")

    st.write(f"**타입:** {result['type']}")
    st.write(f"**추천 이유:** {result['reason']}")
    st.write(f"**한줄 성향:** {result['style']}")

    st.markdown("---")
    st.info("참고: 이 추천은 재미를 위한 성격 매칭 콘텐츠입니다 😄")
else:
    st.caption("MBTI를 선택하면 결과가 표시됩니다.")
