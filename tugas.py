import streamlit as st
import pandas as pd
from modules.text_preprocessing import *
import base64
import io

# Fungsi untuk membuat link download file excel


def get_excel_download_link(df):
    # Untuk mengubah dataframe menjadi excel
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='After')
    writer.save()
    excel_data = output.getvalue()
    b64 = base64.b64encode(excel_data).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="Hasil Proses.xlsx">Download Excel file</a>'
    return href


def create_table(df_spesific):
    counter = 1
    html_syntax = '''
      <tr>
        <th>No</th>
        <th style="text-align: center">Reviews</th>
      </tr>
    '''
    for data in df_spesific:
        html_syntax += f'''<tr style="font-size: 13px">
                <td>{counter}</td>
                <td>{data}</td>
            </tr>
        '''
        counter+=1
    st.write(html_syntax, unsafe_allow_html=True)

def main():
    st.title("Penugasan PPDM Pertama")
    st.markdown(f'''
                    Nama  : I Made Sudarsana Taksa Wibawa
                    \nNIM   : 2108561109
                    \nKelas : D
                    \nLink Github : 
                    <a href="https://github.com/TaksaWibawa/text-preprocessing-ppdm">https://github.com/TaksaWibawa/text-preprocessing-ppdm</a>
                    \n-----
                ''', unsafe_allow_html=True)
    st.sidebar.title("Options")
    file = st.sidebar.file_uploader("Upload a file", type=["xlsx"])
    if file is not None:
        df = pd.read_excel(file)
        st.subheader("Dataset yang diupload")
        st.write(df)

        # buat inputan untuk membatasi jumlah data yang akan diproses dalam streamlit
        st.write("---------")
        st.subheader("Masukan jumlah data yang akan diproses")
        # masukan index awal
        min_data = st.number_input(
            "Masukan index awal", min_value=0, max_value=200, value=0)
        # masukan index akhir
        max_data = st.number_input(
            "Masukan index akhir", min_value=0, max_value=200, value=10)
        # memotong data
        df = df.iloc[min_data:max_data]
        df_before = pd.DataFrame(df, columns=['Reviews'])

        # tambahkan button untuk memproses data
        if (st.button("Proses Data")):
            st.write("---------")
            st.subheader("Before Preprocessing")
            st.write(df_before)

            # Proses Preprocessing
            df_specific = df['Reviews'].tolist()

            st.write("---------")
            st.subheader("1. Case Folding")
            df_specific = [case_folding(sentence) for sentence in df_specific]
            st.dataframe(df_specific)

            st.write("---------")
            st.subheader("2. Tokenizing")
            df_specific = [tokenize(sentence) for sentence in df_specific]
            create_table(df_specific)

            st.write("---------")
            st.subheader("3. Remove Stopwords")
            df_specific = [remove_stopwords(tokens) for tokens in df_specific]
            create_table(df_specific)

            st.write("---------")
            st.subheader("4. Stemming")
            df_specific = [stemming(tokens) for tokens in df_specific]
            st.dataframe(df_specific)

            # Mengubah hasil preprocessing menjadi dataframe
            df_result = pd.DataFrame(df_specific, columns=['Reviews'])

            # Menampilkan hasil dan tombol download file excelnya
            st.write("---------")
            st.subheader("After Preprocessing")
            st.write(df_result)
            st.write("---------")
            st.markdown(get_excel_download_link(
                df_result), unsafe_allow_html=True)

    else:
        st.write("Please upload a file")


if __name__ == "__main__":
    main()
