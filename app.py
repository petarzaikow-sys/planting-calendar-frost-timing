import streamlit as st
import pandas as pd

st.set_page_config(page_title="Кога да засадя?", layout="centered")

st.title("🌱 Кога да засадя?")

# Зареждане на данните
df = pd.read_excel("planting_schedule_final.xlsx")

# Dropdown-и
town = st.selectbox("📍 Избери област", sorted(df["Област"].unique()))
veg = st.selectbox("🥬 Избери зеленчук", sorted(df["Зеленчук"].unique()))

# Филтър
result = df[(df["Област"] == town) & (df["Зеленчук"] == veg)]

if not result.empty:
    row = result.iloc[0]

    st.markdown("---")
    st.subheader("📅 Резултат")

    st.write(f"❄️ Последна слана: **{row['Последна слана']}**")

    st.markdown("### 🌿 Сеитба")
    st.write(f"🟢 Ранна: **{row['Ранна сеитба']}**")
    st.write(f"🟡 Късна: **{row['Късна сеитба']}**")

    if pd.notna(row["Ранно засаждане"]):
        st.markdown("### 🌾 Засаждане")
        st.write(f"🟢 Ранно: **{row['Ранно засаждане']}**")
        st.write(f"🟡 Късно: **{row['Късно засаждане']}**")