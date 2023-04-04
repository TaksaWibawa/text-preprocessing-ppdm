# import pandas as pd
# from modules.text_preprocessing import *
# import streamlit as st

# df = pd.read_excel('data/Dataset D.xlsx')
# df = df.iloc[140:150]
# df_specific = df['Reviews']

# df_specific = df_specific.tolist()
# df_specific = [case_folding(sentence) for sentence in df_specific]
# df_specific = [tokenize(sentence) for sentence in df_specific]
# df_specific = [remove_stopwords(tokens) for tokens in df_specific]
# df_specific = [stemming(tokens) for tokens in df_specific]


# data_before = df['Reviews'].tolist()
# data_before = pd.DataFrame(data_before, columns=['Reviews'])

# data_after = [''.join(df_specific[i]) for i in range(len(df_specific))]
# data_after = pd.DataFrame(data_after, columns=['After Reviews'])

# df_result = pd.concat([data_before, data_after], axis=1)

# df_result.to_excel('data/Dataset D Hasil.xlsx', index=False)
# print("Done!!")

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
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    excel_data = output.getvalue()
    b64 = base64.b64encode(excel_data).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="result.xlsx">Download Excel file</a>'
    return href


def main():
    # Streamlit
    st.title("Penugasan")
    st.sidebar.title("Options")
    file = st.sidebar.file_uploader("Upload a file", type=["xlsx"])
    if file is not None:
        df = pd.read_excel(file)
        df = df.iloc[140:150]
        df_before = pd.DataFrame(df, columns=['Reviews'])
        st.write("Before", df_before)

        # Proses Preprocessing
        df_specific = df['Reviews'].tolist()
        df_specific = [case_folding(sentence) for sentence in df_specific]
        df_specific = [tokenize(sentence) for sentence in df_specific]
        df_specific = [remove_stopwords(tokens) for tokens in df_specific]
        df_specific = [stemming(tokens) for tokens in df_specific]

        # Mengubah hasil preprocessing menjadi dataframe
        df_result = pd.DataFrame(df_specific, columns=['Reviews'])

        # Menampilkan hasil dan tombol download file excelnya
        st.write("After", df_result)
        st.markdown(get_excel_download_link(df_result), unsafe_allow_html=True)
    else:
        st.write("Please upload a file")


if __name__ == "__main__":
    main()
