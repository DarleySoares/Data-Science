import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

def main():
    st.title('Análise Exploratória de Dados')
    file = st.file_uploader('Upload your file:', type = 'csv')
    
    if file is not None:
        df = pd.read_csv(file)
        slider = st.slider('Número de linhas', 1, int(0.1 * df.shape[0]))
        st.subheader('Dataframe')
        st.dataframe(df.head(slider))
        st.subheader('Table')
        st.table(df.head(slider))

def header():
    st.image('images/header.png')
    st.title('Teste')


if __name__ == '__main__':
    header()