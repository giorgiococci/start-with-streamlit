import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main_menu():
    st.title("Vediamo un po' di cose in StreamLit!")
    st.write('In questa dashboard mostreremo un po'' di componenti che Streamlit ci mette a disposizione per creare fantastiche dashboard.')
    st.markdown('Possiamo *anche* aggiungere un **po''** di ***markdown*** per dare un stile alla nostra pagina.')

    st.write('Stampiamo anche un dataframe di Pandas: ')

    df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})
    st.write(df)

    # Si può fare anche in questo modo:
    # st.dataframe(df)

    st.write("Con Streamlit possiamo anche colorare delle celle del Dataframe. Ad esempio evidenziamo il valore massimo per ogni colonna")

    df = pd.DataFrame(np.random.randn(10, 20),columns=('col %d' % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))

    st.header("Adesso passiamo ai grafici!")
    st.write("Streamlit supporta diverse librerie per disegnare grafici, tra cui **matplotlib**, più alcuni grafici si possono costruire nativamente.")

    st.write("I primi due grafici sono fatti nativamente con Streamlit:")
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c']) 
    st.line_chart(chart_data)

    st.bar_chart(chart_data)

    st.write("Questo è un esempio con matplotlib:")

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

    st.write("Esempio di una mappa con Streamlit:")

    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon']) 
    st.map(df)

    st.write("E' possibile anche inserire delle immagini...")


if __name__ == "__main__":
    main_menu()