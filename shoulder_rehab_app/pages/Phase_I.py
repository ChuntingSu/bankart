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
    "Completion of 6 weeks post-surgery",
    "Pain and inflammation controlled"
]
for c in criteria:
    st.write(f"- {c}")

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
    "ER ≤ 10°, IR ≤ 30° (pain-free)"
]
for r in rom:
    st.write(f"- {r}")
