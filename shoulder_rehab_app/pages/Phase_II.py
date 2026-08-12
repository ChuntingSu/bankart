import streamlit as st

st.title("Phase II – Protection (Week 7–14)")

st.header("🎯 Goals")
goals = [
    "Gradually restore full ROM (by week 10)",
    "Preserve integrity of repair",
    "Restore muscle strength and balance",
    "Enhance neuromuscular control"
]
for g in goals:
    st.write(f"- {g}")

st.header("✅ Criteria to Enter Next Phase")
criteria = [
    "Full non-painful ROM",
    "Satisfactory stability",
    "Good muscle strength"
]
for c in criteria:
    st.write(f"- {c}")

st.header("📝 Plan")
plan = [
    "Continue isotonic and manual strengthening",
    "Progress ROM to functional demands",
    "Begin plyometric program (2-hand drills by week 14)"
]
for p in plan:
    st.write(f"- {p}")

st.header("📏 ROM Limitation")
rom = [
    "Flexion ≤ 160°",
    "ER ≤ 90° at 90° abduction",
    "IR ≤ 60° at 90° abduction"
]
for r in rom:
    st.write(f"- {r}")
