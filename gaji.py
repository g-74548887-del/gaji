import streamlit as st
import json
import os

DATA_FILE = "data.json"

# ======================
# LOAD / SAVE DATA
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
st.title("📒 Urusan Kewangan Gaji")

bulan = st.text_input(
    "Tajuk Gaji (contoh: Gaji Februari 2026)",
    placeholder="Gaji Bulan ______"
)

if not bulan:
    st.stop()

if bulan not in data:
    data[bulan] = {"items": {}}

items = data[bulan]["items"]

st.subheader("💰 Senarai Perbelanjaan")

to_delete = []

for nama, status in items.items():
    if not status:
        if st.checkbox(nama):
            items[nama] = True
            to_delete.append(nama)

# Hilangkan yang dah tick
for d in to_delete:
    del items[d]

# ======================
# TAMBAH ITEM BARU
# ======================
st.divider()
st.subheader("➕ Tambah Urusan Baru")

new_item = st.text_input("Nama urusan (contoh: Loan Kereta RM507)")

if st.button("Tambah"):
    if new_item:
        items[new_item] = False
        save_data(data)
        st.success("Berjaya tambah!")
        st.experimental_rerun()

save_data(data)

st.divider()
st.info("✔️ Yang dah tick akan hilang\n📂 Data automatik disimpan\n🔄 Bulan baru = list reset")
