import streamlit as st
import random

st.set_page_config(
    page_title="나의 MBTI 포켓몬",
    page_icon="⚡",
    layout="centered"
)

POKEMON = {
    "INTJ": ("뮤츠", "🧬", "강한 독립심과 뛰어난 전략 능력을 가진 전설의 포켓몬!", "혼자 있는 듯 보여도 머릿속에서는 세계 정복 계획을 세우는 중입니다."),
    "INTP": ("메타몽", "🟣", "무한한 가능성과 독특한 사고방식을 가진 변신의 천재!", "관심 있는 분야를 만나면 어떤 모습으로든 진화할 수 있습니다."),
    "ENTJ": ("리자몽", "🔥", "강한 카리스마로 목표를 향해 날아가는 리더형 포켓몬!", "당신이 방향을 정하면 동료들은 자연스럽게 따라옵니다."),
    "ENTP": ("팬텀", "👻", "장난기와 아이디어가 넘치는 예측 불가능한 포켓몬!", "평범한 길보다 재미있는 지름길을 발견하는 능력이 있습니다."),

    "INFJ": ("루카리오", "💫", "상대의 마음과 분위기를 섬세하게 감지하는 포켓몬!", "조용하지만 소중한 사람을 위해서는 누구보다 강해집니다."),
    "INFP": ("이브이", "🌟", "따뜻한 감성과 다양한 가능성을 품고 있는 포켓몬!", "어떤 모습으로 성장할지는 당신의 선택에 달려 있습니다."),
    "ENFJ": ("가디안", "🔮", "사람들을 보호하고 이끄는 따뜻한 수호자 포켓몬!", "주변 사람들의 잠재력을 발견하는 특별한 눈을 가졌습니다."),
    "ENFP": ("피카츄", "⚡", "밝은 에너지로 모두를 즐겁게 만드는 인기 포켓몬!", "어디를 가든 새로운 친구와 새로운 모험이 생깁니다."),

    "ISTJ": ("거북왕", "💧", "책임감과 안정적인 실력을 갖춘 믿음직한 포켓몬!", "말보다는 확실한 결과로 능력을 증명하는 타입입니다."),
    "ISFJ": ("해피너스", "💗", "주변 사람을 세심하게 돌보는 따뜻한 포켓몬!", "당신 곁에 있으면 이상하게 마음이 편안해집니다."),
    "ESTJ": ("망나뇽", "🐉", "강한 실행력과 든든함을 겸비한 리더 포켓몬!", "해야 할 일을 발견하면 고민보다 행동이 먼저입니다."),
    "ESFJ": ("님피아", "🎀", "친화력과 다정함으로 분위기를 밝히는 포켓몬!", "모임에서 모두가 즐거운지 가장 먼저 살펴봅니다."),

    "ISTP": ("개굴닌자", "🥷", "침착하고 민첩하게 문제를 해결하는 포켓몬!", "설명은 짧게, 행동은 빠르고 정확하게 움직입니다."),
    "ISFP": ("파치리스", "🌿", "자유롭고 사랑스러운 매력을 지닌 감성 포켓몬!", "조용히 있다가 결정적인 순간에 모두를 놀라게 합니다."),
    "ESTP": ("에이스번", "⚽", "도전과 경쟁을 즐기는 행동파 포켓몬!", "일단 뛰어들고 현장에서 답을 찾아내는 스타일입니다."),
    "ESFP": ("고라파덕", "💛", "엉뚱하지만 미워할 수 없는 매력의 분위기 메이커!", "본인은 평범하게 행동했는데 주변에서는 이미 웃고 있습니다.")
}

REACTIONS = [
    "포켓몬 도감과 성격 파장이 완벽하게 일치했습니다!",
    "오박사님도 결과를 보고 고개를 끄덕였습니다.",
    "야생의 포켓몬이 당신을 동료로 선택했습니다!",
    "이 조합은 생각보다 강력합니다. 배틀 신청 주의!",
    "당신의 가방에서 몬스터볼이 흔들리고 있습니다!"
]

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
    }
    .result-box {
        padding: 25px;
        border-radius: 20px;
        background: linear-gradient(135deg, #fff5c2, #ffe0e9);
        text-align: center;
        margin-top: 20px;
        color: #222;
    }
    .pokemon {
        font-size: 4.5rem;
        margin: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">⚡ MBTI 포켓몬 연구소 ⚡</div>',
            unsafe_allow_html=True)
st.caption("당신의 성격과 가장 잘 어울리는 포켓몬을 찾아보세요!")

mbti = st.selectbox(
    "나의 MBTI를 선택하세요",
    ["선택하기"] + list(POKEMON.keys())
)

if st.button("🔴 몬스터볼 열기", use_container_width=True):
    if mbti == "선택하기":
        st.warning("먼저 MBTI를 선택해주세요!")
    else:
        name, emoji, description, comment = POKEMON[mbti]

        st.balloons()
        st.markdown(
            f"""
            <div class="result-box">
                <div>당신과 함께할 포켓몬은...</div>
                <div class="pokemon">{emoji}</div>
                <h1>{name}</h1>
                <h3>{mbti} × {name}</h3>
                <p>{description}</p>
                <p><b>💬 포켓몬 분석:</b> {comment}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(random.choice(REACTIONS))
        st.progress(random.randint(85, 100), text="포켓몬 궁합 분석 완료!")

st.divider()
st.caption("※ 재미로 보는 성격 테스트입니다. 포켓몬 배틀 결과는 책임지지 않습니다 😄")
