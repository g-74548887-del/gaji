import streamlit as st
import json
import os

DATA_FILE = "data.json"

# ======================
# LOAD & SAVE
# ======================
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# ======================
# UI
# ======================
st.title("📒 Pengurusan Gaji Bulanan")

bulan = st.text_input(
    "Tajuk Gaji (contoh: Gaji Februari 2026)",
    placeholder="Gaji Bulan ______"
)

if not bulan:
    st.warning("Sila isi tajuk gaji dahulu")
    st.stop()

# Jika bulan baru
if bulan not in data:
    data[bulan] = {"items": {}}

items = data[bulan]["items"]

# ======================
# SENARAI URUSAN
# ======================
st.subheader("💰 Senarai Urusan Kewangan")

if not items:
    st.info("Tiada urusan lagi. Tambah di bawah 👇")

to_remove = []

for nama, status in list(items.items()):
    if status is False:
        if st.checkbox(nama, key=nama):
            items[nama] = True
            to_remove.append(nama)

# Buang yang dah dibayar (hilang)
for r in to_remove:
    del items[r]

save_data(data)

# ======================
# TAMBAH ITEM BARU
# ======================
st.divider()
st.subheader("➕ Tambah Urusan Baru")

new_item = st.text_input(
    "Nama urusan (contoh: Loan Kereta RM507)",
    key="new_item"
)

if st.button("Tambah"):
    if new_item.strip() == "":
        st.error("Nama urusan tak boleh kosong")
    else:
        items[new_item] = False
        save_data(data)
        st.success("Berjaya tambah!")
        st.rerun()

# ======================
# INFO
# ======================
st.divider()
st.info(
    "✔️ Tick = dah bayar (auto hilang)\n"
    "📂 Data automatik disimpan\n"
    "🔄 Bulan baru = senarai reset\n"
    "📱 Sesuai untuk Pydroid & Streamlit Cloud"
)
