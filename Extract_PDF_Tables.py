import tempfile
import streamlit as st
from settings import *
from streamlit_lottie import st_lottie
import streamlit as st
import tabula as tb 
import pandas as pd

# streamlit run Extract_PDF_Tables.py

st.set_page_config(page_title=TITLE,
    layout="wide")


st.markdown("<h2 style=\
        'text-align : center';\
        font-weight : bold ;\
        font-family : Arial;>\
        Extract Tables from PDF</h2>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar :

    uploaded_file2 = st.file_uploader("📌 Upload PDF", type=["pdf"], key="fup2", label_visibility="visible")

if uploaded_file2 :
    try :
        with st.spinner("Extraction in progress, please wait...") :
            tables = tb.read_pdf(uploaded_file2, pages = "all")

        if len(tables)==0:
            st.error("No table detected")

        else :
            colpi1_t, colpi2_t, colpi3_t = st.columns([42, 16, 42])

            with colpi2_t:
                st.markdown(f"<h5 style=\
                'text-align : left';\
                font-weight : bold ;\
                font-family : Arial;>\
                <b>{len(tables)} Tables Detected</h5></b>", unsafe_allow_html=True)

                tabe_idx = st.number_input(label="Label", value=1, min_value=1,
                    max_value=len(tables), step=1, label_visibility="collapsed")

            temp = tempfile.NamedTemporaryFile(delete=True)
            temp_filename = temp.name + f'.xlsx'

            with pd.ExcelWriter(temp_filename) as writer:
                for i in range (len(tables)):
                    tables[i].to_excel(writer, sheet_name=f"table{i}")

            with open(writer, "rb") as f:
                binary_data = f.read()

            excel_namefile = f"Tables_{uploaded_file2.name[:-4]}.xlsx"

            st.download_button(
                label="Download Excel File",
                data=binary_data,
                file_name=excel_namefile)

            st.markdown(f"<p style=\
            'text-align : left';\
            font-weight : bold ;\
            font-family : Arial;>\
            <b><u>Table Displayed :</u> {tabe_idx} / {len(tables)}</p></b>", unsafe_allow_html=True)

            st.dataframe(tables[tabe_idx-1].style.format(na_rep='No Data', precision=1), use_container_width=True)
    
    except:
        st.markdown("<br>", unsafe_allow_html=True)
        st.error("This tool is not available due to disruptions on one of the\
            libraries used, a fix is in progress.")


else:
    st.markdown("<br>", unsafe_allow_html=True)
    colpi_1, colpi_2 = st.columns([85, 15], gap="small")
    with colpi_1 :
        st.info("This tool allows you to extract tables from a PDF : \
            \n ● View them directly on the app\
            \n ● Save them to your machine in Excel format\
            \n\n You can upload the PDF to be processed on the left menu")

    with colpi_2:
        lottie_pdf_table = load_lottiefile(lottie_pdf_table)
        st_lottie(
        lottie_pdf_table,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=150)
