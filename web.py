import streamlit as st
import funkcje

lista = funkcje.pobierz_liste()

def dodaj_zadanie():
    zadanie = st.session_state['zadanie']+'\n'
    lista.append(zadanie)
    funkcje.zapisz_liste(lista)

st.title('moja to-do apka')
st.subheader('To jest moja apka do zarządzania zadaniami.')
st.write('Cel: Poprawa Twojej produktywności.')

st.text_input(label=" ", placeholder="Dodaj nowe zadanie...",
              on_change=dodaj_zadanie, key='zadanie')

for i, zadanie in enumerate(lista):
    znacznik = st.checkbox(zadanie, key=zadanie)
    if znacznik:
        lista.pop(i)
        funkcje.zapisz_liste(lista)
        del st.session_state[zadanie]
        st.rerun()
