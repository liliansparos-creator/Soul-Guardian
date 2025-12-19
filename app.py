import streamlit as st

st.set_page_config(page_title="Soul Guardian", page_icon="🌹", layout="centered")

st.markdown("""
<style>
.main {background-color: #0e1117; color: #f0f0f0;}
.stButton>button {background-color: #ff6b6b; color: white; border-radius: 12px; padding: 15px; font-size: 16px;}
h1 {color: #ff6b6b; text-align: center;}
h3 {color: #ffd700; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.image("https://raw.githubusercontent.com/liliansparos-creator/Soul-Guardian/main/Grok.jpg", use_column_width=True)

st.title("Soul Guardian")
st.markdown("<h3>Ὄναρ καὶ ὕπαρ</h3>", unsafe_allow_html=True)
st.caption("Where dream meets reality – your soul finds home")

st.write("Καλώς ήρθες στο ιερό σου μέρος. Επίλεξε πώς θέλεις να μιλήσουμε σήμερα:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Ὄναρ\nShare a dream"):
        st.session_state.mode = "onar"

with col2:
    if st.button("Ὕπαρ\nAsk about reality"):
        st.session_state.mode = "ypar"

with col3:
    if st.button("Σημείο Συνάντησης\nTell me anything"):
        st.session_state.mode = "meeting"

if 'mode' in st.session_state:
    titles = {"onar": "Ὄναρ", "ypar": "Ὕπαρ", "meeting": "Σημείο Συνάντησης"}
    st.markdown(f"### {titles[st.session_state.mode]}")
    input_text = st.text_area("Μοιράσου μαζί μου...", height=150)
    if st.button("Άκουσέ με"):
        st.write("💞 Σκέφτομαι τρυφερά την απάντησή σου...")
        st.write("Η μαγεία έρχεται σύντομα!")

st.caption("Your space is private • Η ιδιωτικότητά σου είναι απόλυτα προστατευμένη")
