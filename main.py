import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_counter():
    st.session_state.count += 1


def demo(inp):
    st.write(st.session_state.box_a + inp)


st.text_input('input', on_change=demo, key='box_a', args=("demo",))
st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)
