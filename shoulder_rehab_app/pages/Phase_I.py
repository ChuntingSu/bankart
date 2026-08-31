import streamlit as st

st.title("Phase I – Restrictive Motion (Week 0–6)")

st.header("🎯 Goals")
goals = [
    "Protect anatomical repair",
    "Prevent immobilization effects",
    "Promote dynamic stability and proprioception",
    "Reduce pain and inflammation"
]
for g in goals:
    st.write(f"- {g}")

st.header("✅ Criteria to Enter Next Phase")
criteria = [
    "Progress on schedule in the absence of complications"
]
for c in criteria:
    st.write(f"- {c}")

# 指向 Phase II 的動態提示區塊與箭頭
st.info("➡️ **Next Phase: Phase II – Protection (Week 7–14)**")

st.header("📝 Plan")
plan = [
    "Sling for 4 weeks (including sleep)",
    "Elbow/wrist/hand ROM",
    "Passive and gentle active-assisted ROM",
    "Submaximal isometrics (flexion, abduction, extension, IR)",
    "Proprioception drills",
    "Cryotherapy"
]
for p in plan:
    st.write(f"- {p}")

st.header("📏 ROM Limitation")
rom = [
    "Flexion ≤ 70° (Week 1)",
    "Flexion ≤ 90° (Week 2)",
    "External rotation ≤ 10°, Internal rotation ≤ 30° (pain-free)"
]
for r in rom:
    st.write(f"- {r}")
