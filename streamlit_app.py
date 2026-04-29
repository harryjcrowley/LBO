import streamlit as st
import openpyxl

st.title("LBO Converter Tool")
st.divider()
uploaded_file = st.file_uploader("Upload engage file:")
if uploaded_file is not None:
    to_add=None
    import pandas as pd
    df=pd.read_csv(uploaded_file)
    new=df[df['CurrentStepName']=='SGA Finance Committee Approval']
    print(new.head())
    new=new.drop(columns=['Id',
                    'ProcessName',
                    'SubmitterName',
                    'SubmitterEmail',
                    'LastSubmitted',
                    'Status',
                    'CurrentStepName',
                    'BudgetName',
                    'SectionName',
                    'LineItemName'])
    new['FirstSubmitted']=new['FirstSubmitted'].str[0:10]
    ordered=new[['FirstSubmitted', 'SubmittedOnBehalfOf', 'Title', 'RequestedAmount', 'AdjustedAmount']]
    to_add=st.text_input('Date of committee meeting (MM/DD/YYYY): ')
    if len(to_add)==10:
        num=len(ordered)
        dates=[]
        for f in range(num):
            dates.append(to_add)
        ordered['FC Date']=dates
        from io import BytesIO
        buffer = BytesIO()
        ordered.to_excel(buffer, sheet_name='Data', index=False)
        buffer.seek(0)

        st.download_button(
            label="Download data as excel file",
            data=buffer.getvalue(),
            file_name='formatted.xlsx',
            mime='text/csv',)
    
st.badge("v1.0 | Created by Harry Crowley", color='blue')