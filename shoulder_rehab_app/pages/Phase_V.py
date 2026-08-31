import streamlit as st

st.title("Phase V – Return to Activity (Month 7–9)")

st.header("🎯 Goals")
goals = [
    "Gradual return to sport activities",
    "Maintain strength, mobility, and stability"
]
for g in goals:
    st.write(f"- {g}")

st.header("✅ Criteria to Enter Next Phase")
criteria = [
    "Absence of pain or tenderness",
    "≥ 6 months post-surgery",
    "Full functional ROM (≥90% LSI)",
    "Strength ≥90% of contralateral side",
    "Satisfactory shoulder stability",
    "Psychological readiness (SIRSI)"
]
for c in criteria:
    st.write(f"- {c}")

# 指向 Return to Sport 的最終解封提示區塊與箭頭
st.success("➡️ **Next Stage: FULL RETURN TO SPORT (Unrestricted Participation)**")

st.header("📝 Plan")
plan = [
    "Progress to unrestricted participation",
    "Continue maintenance mobility and strengthening"
]
for p in plan:
    st.write(f"- {p}")

st.header("📏 ROM Limitation")
rom = [
    "Full unrestricted ROM",
    "No limitations"
]
for r in rom:
    st.write(f"- {r}")
