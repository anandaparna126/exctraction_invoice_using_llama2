import streamlit as st
from dotenv import load_dotenv
from utils import create_docs
from utils import get_pdf_text
from utils import extracted_data


def main():
    load_dotenv()

    st.set_page_config(page_title="extraction using LLAMA2")
    st.title("extraction using LLAMA2")
    st.subheader("I can help you in extracting invoice data")

    # upload the invoices (pdf files)
    pdf = st.file_uploader("Upload the invoices in pdf format here..", type = ['pdf'], accept_multiple_files=True)

    submit=st.button("Extract Data")

    if submit:
        with st.spinner("wait for it...."):
            df = create_docs(pdf)
            st.write(df.head())

            data_as_csv = df.to_csv(index = False).encode("utf-8")
            st.download_button("Download the data as csv",
                               data_as_csv,
                               "invoice_extracted_data.csv",
                               "text/csv",
                               key = "download_tools-csv",
                               )

        st.success("Hope I was able to save your time.")

# invoking main function
if __name__ == '__main__':
    main()