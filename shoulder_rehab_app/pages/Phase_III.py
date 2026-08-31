import streamlit as st

st.title("Phase III – Minimal Protection (Week 15–20)")

st.header("🎯 Goals")
goals = [
    "Maintain full ROM",
    "Improve muscle strength, power, and endurance",
    "Gradually initiate functional activities"
]
for g in goals:
    st.write(f"- {g}")

st.header("✅ Criteria to Enter Next Phase")
criteria = [
    "Full non-painful ROM",
    "Satisfactory stability",
    "Muscular strength (good grade)",
    "No pain or tenderness"
]
for c in criteria:
    st.write(f"- {c}")

# 指向 Phase IV 的動態提示區塊與箭頭
st.info("➡️ **Next Phase: Phase IV – Advanced Strengthening (Week 21–24)**")

st.header("📝 Plan")
plan = [
    "Continue mobility and strengthening",
    "Full throwers program",
    "Resistance and endurance training",
    "Progress plyometric to 1-hand drills (week 18)"
]
for p in plan:
    st.write(f"- {p}")

st.header("📏 ROM Limitation")
rom = [
    "Full ROM achieved",
    "Pain-free movement in all planes"
]
for r in rom:
    st.write(f"- {r}")
