import streamlit as st
import pandas as pd

# Настройки на страницата
st.set_page_config(
    page_title="Кога да засадя?",
    layout="centered"
)

# Заглавие
st.title("🌱 Кога да засадя?")

# Зареждане на данните
df = pd.read_excel("planting_schedule_final.xlsx")

# Dropdown избори
town = st.selectbox(
    "📍 Избери област",
    sorted(df["Област"].unique()),
    index=None,
    placeholder="Избери област..."
)

veg = st.selectbox(
    "🥬 Избери зеленчук",
    sorted(df["Зеленчук"].unique()),
    index=None,
    placeholder="Избери зеленчук..."
)

st.markdown("---")

# Бутон за резултат
if st.button("🔍 Покажи резултат"):

    # Проверка дали има избор
    if town is None or veg is None:
        st.warning("Моля избери област и зеленчук.")
    else:
        result = df[
            (df["Област"] == town) &
            (df["Зеленчук"] == veg)
        ]

        if not result.empty:
            row = result.iloc[0]

            st.subheader("📅 Резултат")

            # Основна информация
            st.write(f"❄️ Последна слана: **{row['Последна слана']}**")

            # Сеитба
            st.markdown("### 🌿 Сеитба")
            st.write(f"🟢 Ранна: **{row['Ранна сеитба']}**")
            st.write(f"🟡 Късна: **{row['Късна сеитба']}**")

            # Засаждане (само ако съществува)
            if pd.notna(row["Ранно засаждане"]):
                st.markdown("### 🌾 Засаждане")
                st.write(f"🟢 Ранно: **{row['Ранно засаждане']}**")
                st.write(f"🟡 Късно: **{row['Късно засаждане']}**")

# Разделител
st.markdown("---")

# Важно уточнение
st.info(
    "ℹ️ Важно: Посочените дати са ориентировъчни. "
    "Те са базирани на осреднени данни от предходни години. "
    "Реалните условия могат да варират според времето и конкретната година."
)
