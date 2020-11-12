import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image

def main_menu():
    st.title("Vediamo un po' di cose in StreamLit!")
    st.write('In questa dashboard mostreremo un po'' di componenti che Streamlit ci mette a disposizione per creare fantastiche dashboard.')
    st.markdown('Possiamo *anche* aggiungere un **po''** di ***markdown*** per dare un stile alla nostra pagina.')

    df_expander = st.beta_expander("Dataframe")
    df_expander.write('Stampiamo anche un dataframe di Pandas: ')

    df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
    df_expander.write(df)

    # Si può fare anche in questo modo:
    # st.dataframe(df)

    df_expander.write("Con Streamlit possiamo anche colorare delle celle del Dataframe. Ad esempio evidenziamo il valore massimo per ogni colonna")

    df = pd.DataFrame(np.random.randn(10, 20),columns=('col %d' % i for i in range(20)))
    df_expander.dataframe(df.style.highlight_max(axis=0))

    charts_expander = st.beta_expander("Charts")

    charts_expander.header("Adesso passiamo ai grafici!")
    charts_expander.write("Streamlit supporta diverse librerie per disegnare grafici, tra cui **matplotlib**, più alcuni grafici si possono costruire nativamente.")

    charts_expander.write("I primi due grafici sono fatti nativamente con Streamlit:")
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']) 
    charts_expander.line_chart(chart_data)

    charts_expander.bar_chart(chart_data)

    charts_expander.write("Questo è un esempio con matplotlib:")

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    charts_expander.pyplot(fig)

    charts_expander.write("Esempio di una mappa con Streamlit:")

    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon']) 
    charts_expander.map(df)


    image_expander = st.beta_expander("Images")
    image_expander.write("E' possibile anche inserire delle immagini...")
    image = Image.open('static/reti-campus.png')
    image_expander.image(image, use_column_width=True)

def side_menu():
    st.sidebar.title("Questa è la sidebar!")
    st.sidebar.write("Qui puoi inserire dei widget dinamici per interagire con la pagina e i dati.")

    if(st.sidebar.checkbox('Show line chart')):
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

    age = st.sidebar.selectbox("Seleziona la tua fascia di età", ["0-10", "11-20", "21-30", "31-40", "41-50", "> 50"])

    df_number = pd.DataFrame(np.random.randn(10,1), columns=['num'])

    random_number = st.sidebar.selectbox("Quale numero preferisci?", df_number['num'])

    range_number = st.sidebar.slider("Scegli un altro numero in questo range", 0, 20, 5, 1)

    free_text = st.sidebar.text_input("Inserisci quello che vuoi")

    if(st.sidebar.button('Stampa le tue scelte')):
        st.success("Hai fatto una selezione corretta!!")
        st.markdown('**Le tue scelte sono:**')
        st.write(f'Age: {age}')
        st.write(f'Random Number: {random_number}')
        st.write(f'Range Number: {range_number}')
        st.write(f'Free Text: {free_text}')


    st.sidebar.write("Comanda il grafico")

    df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    column = st.sidebar.multiselect(
        'Quali colonne vuoi mostrare?',
        df.columns)

    st.line_chart(df[column])

if __name__ == "__main__":
    main_menu()
    side_menu()