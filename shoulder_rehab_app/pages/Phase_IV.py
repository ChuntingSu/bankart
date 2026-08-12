import streamlit as st

st.title("Phase IV – Advanced Strengthening (Week 21–24)")

st.header("🎯 Goals")
goals = [
    "Enhance muscular strength, power, and endurance",
    "Progress functional activities",
    "Maintain shoulder mobility"
]
for g in goals:
    st.write(f"- {g}")

st.header("✅ Criteria to Enter Next Phase")
criteria = [
    "Full non-painful ROM",
    "Satisfactory stability",
    "Strength ≥ 75–80% of contralateral side",
    "No pain or tenderness"
]
for c in criteria:
    st.write(f"- {c}")

st.header("📝 Plan")
plan = [
    "Continue isotonic and proprioceptive drills",
    "Continue plyometric strengthening",
    "Begin interval sport programs"
]
for p in plan:
    st.write(f"- {p}")

st.header("📏 ROM Limitation")
rom = [
    "Full ROM maintained",
    "No restrictions"
]
for r in rom:
    st.write(f"- {r}")
