from UploadRatesModule import upload_rates
from UploadAllotmentsModule import upload_allotments
from UploadStopSalesModule import upload_stopsales
from UploadReleaseModule import upload_release
from UploadRestrictionsModule import upload_restriction_with_minstay, upload_restriction_with_checkinorcheckout
from UploadSupplementsModule import upload_basic_supplement_per_room, upload_basic_supplement_per_shortstay, upload_basic_supplement_per_person
import streamlit as st
st.set_page_config(layout='wide',page_icon="📜")
import requests
import bcrypt
import numpy as np
import pandas as pd
import xmltodict
from tqdm.notebook import tqdm
import aiohttp
import asyncio
import warnings
from datetime import datetime
import aiohttp
import asyncio
import numpy as np
from GetHotelData import return_hoteldata, return_hotelcontracts
import firebase_admin
from firebase_admin import credentials,db
warnings.filterwarnings("ignore")

if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\Administrator\Desktop\EET Contracting System\credentials.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://contractuploader-5aad6-default-rtdb.firebaseio.com/"
    })
    
ref = db.reference('/')
data = ref.get()
#print(data) 

st.title("EET Contract Uploader System")

with st.sidebar:
    st.image("images/ImageRequest.png", use_column_width=True)
    
url="https://www.eetglobal.com/webservicejpdm/operations/hotelextranettransactions.asmx"
headers = {'content-type': 'text/xml','SOAPAction':'http://www.juniper.es/webservice/2007/ExtranetHotelRatesUpdate',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"}

USERNAME = "EET"
HASHED_PASSWORD = b'$2b$12$SAcNKXMnO0SQ20FhVhqz6.1b6kacV6BZJiCIrUsPQwxwTfQe1hXVO'

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def retrun_message_error(response):
    if response.status_code == 200:
        try:
            error = xmltodict.parse(response.text)['soap:Envelope']['soap:Body']['ExtranetHotelRatesUpdateResponse']['ExtranetRatesUpdRS']['Errors']['Error']['Text']
        except:
            error = "No Error"

        if error != "No Error":
            st.error(f"You have an error in line {i+1}, Error is: {error}") 
        else:
            st.success(f"Line {i+1}, Success")
    else:
        st.error(f"You have an error in line {i+1}, Bad Request")
    
juniper_user = ""
juniper_pass = ""
def signin():
    global juniper_user
    global juniper_pass
    st.sidebar.title('Sign in')
    username = st.sidebar.text_input("Enter user name:", key="user",placeholder="Enter use name")
    password = st.sidebar.text_input("Enter Password:", key="password",placeholder="Enter password",type="password")
    if st.sidebar.checkbox("Login"):
        check = 0
        for user in data:
            if user['Name'].lower() == username.lower() and user['Password']==password:
                check = 1
                st.sidebar.success("Login successful!")
                juniper_user = user['Apiuser']
                juniper_pass = user['ApiPass']
                return True
        if check == 0:
            st.sidebar.warning("Enter the correct username and password.")


def build_body(x):
    body = f"""<soapenv:Envelope xmlns:soapenv = "http://schemas.xmlsoap.org/soap/envelope/" xmlns = "http://www.juniper.es/webservice/2007/">
        <soapenv:Header/>
        <soapenv:Body>
            <ExtranetHotelRatesUpdate>
                <HotelRatesUpdateRQ Version = "1.1" Language = "en">
                    <Login Email = "{juniper_user}" Password = "{juniper_pass}"/>
                    {x}
                </HotelRatesUpdateRQ>
            </ExtranetHotelRatesUpdate>
        </soapenv:Body>
    </soapenv:Envelope>"""
    return body
    
if signin():
    st.markdown(f":green[*Welcome {juniper_user}* 😃]")
    option = st.selectbox(
            "What you want to update?",
            ("Get Hotel Data","Rates", "Allotments", "Stop Sales","Releases","Restrictions","Supplements"),
        )
    
    if option == "Get Hotel Data":
        hbe_code = st.text_input("Enter the HBE Code",placeholder="Enter HBE Code")
        if st.button("Get the Hotel Data",use_container_width=True,type="primary"):
            try:
                df2 = return_hotelcontracts(hbe_code)
                with st.expander("Extranet Hotel Contracts",expanded=False):
                    st.dataframe(df2,use_container_width=True)
            except:
                with st.expander("Extranet Hotel Contracts",expanded=False):
                    st.error(f"Please Make sure from the Hotel Code or this hotel contains extranet contracts")
            try:
                df = return_hoteldata(hbe_code)
                with st.expander("Hotel Rooms",expanded=False):
                    st.dataframe(df,use_container_width=True)
            except:
                with st.expander("Hotel Rooms",expanded=False):
                    st.error(f"Please Make sure from the Hotel Code")
    else:
        uploaded_file = st.file_uploader(f"Upload {option} sheet")


        if uploaded_file is not None:
            
            
            if option == "Rates":
                if st.button(f"Upload {option}",use_container_width=True,type="primary"):
                    df = pd.read_excel(uploaded_file)
                    try:
                        df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        for i,row in df.iterrows():
                            try:
                                x = upload_rates(row)
                            except:
                                st.error(f"Please Make sure from the template and headers names")
                                break
                            body = build_body(x)
                            response = requests.post(url, headers=headers, data=body)
                            retrun_message_error(response)
                    except:
                        if 'From' in df.columns and 'To' in df.columns:
                            st.error(f"Please check the date format, Should be (Year-Month-day)")
                        else:
                            st.error(f"Please Make sure from the template and headers names")
                            
                    
                        
                            
            elif option == "Allotments":
                if st.button(f"Upload {option}",use_container_width=True,type="primary"):
                    df = pd.read_excel(uploaded_file)
                    try:
                        df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        for i,row in df.iterrows():
                            try:
                                x = upload_allotments(row)
                            except:
                                st.error(f"Please Make sure from the template and headers names")
                                break
                            body = build_body(x)
                            response = requests.post(url, headers=headers, data=body)
                            retrun_message_error(response)
                    except:
                        if 'From' in df.columns and 'To' in df.columns:
                            st.error(f"Please check the date format, Should be (Year-Month-day)")
                        else:
                            st.error(f"Please Make sure from the template and headers names")
                    
            elif option == "Stop Sales":
                action = st.selectbox("What you need to do?",("OnRequest", "Close", "Open" ),)
                if st.button(f"Upload {option}",use_container_width=True,type="primary"):
                    df = pd.read_excel(uploaded_file)
                    try:
                        df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        for i,row in df.iterrows():
                            try:
                                x = upload_stopsales(row,action)
                            except:
                                st.error(f"Please Make sure from the template and headers names")
                                break
                            body = build_body(x)
                            response = requests.post(url, headers=headers, data=body)
                            retrun_message_error(response)
                    except:
                        if 'From' in df.columns and 'To' in df.columns:
                            st.error(f"Please check the date format, Should be (Year-Month-day)")
                        else:
                            st.error(f"Please Make sure from the template and headers names")
                            
            elif option == "Releases":
                if st.button(f"Upload {option}",use_container_width=True,type="primary"):
                    df = pd.read_excel(uploaded_file)
                    try:
                        df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        for i,row in df.iterrows():
                            try:
                                x = upload_release(row)
                            except:
                                st.error(f"Please Make sure from the template and headers names")
                                break
                            body = build_body(x)
                            response = requests.post(url, headers=headers, data=body)
                            retrun_message_error(response)
                    except:
                        if 'From' in df.columns and 'To' in df.columns:
                            st.error(f"Please check the date format, Should be (Year-Month-day)")
                        else:
                            st.error(f"Please Make sure from the template and headers names")
                            
                            
            elif option == "Restrictions":
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                weekDays = []
                col1, col2 = st.columns(2)
                with col1:
                    restriction_Types = st.selectbox("What is The Restriction Type?",("MinimumStay", "CheckinDays", "CheckoutDays"),)
                    
                if restriction_Types == "CheckinDays" or restriction_Types == "CheckoutDays":
                    with col2:
                        days_options = st.multiselect("Choose the days?",["All","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],default=["All"],)
                    if "All" in days_options:
                        weekDays.append("X"*7)
                    else:
                        for d in days:
                            if d in days_options:
                                weekDays.append("X")
                            else:
                                weekDays.append("-")
                    weekDays = "".join(weekDays)
                    if st.button(f"Upload {option} with {restriction_Types}",use_container_width=True,type="primary"):
                        df = pd.read_excel(uploaded_file)
                        try:
                            df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                            df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                            for i,row in df.iterrows():
                                x = upload_restriction_with_checkinorcheckout(row,restriction_Types,weekDays)
                                try:
                                    body = build_body(x)
                                except:
                                    st.error(f"Please Make sure from the template and headers names")
                                    break
                                response = requests.post(url, headers=headers, data=body)
                                retrun_message_error(response)
                        except:
                            if 'From' in df.columns and 'To' in df.columns:
                                st.error(f"Please check the date format, Should be (Year-Month-day)")
                            else:
                                st.error(f"Please Make sure from the template and headers names")
                else:
                    if st.button(f"Upload {option} with {restriction_Types}",use_container_width=True,type="primary"):
                        df = pd.read_excel(uploaded_file)
                        try:
                            df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                            df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                            for i,row in df.iterrows():
                                x = upload_restriction_with_minstay(row)
                                try:
                                    body = build_body(x)
                                except:
                                    st.error(f"Please Make sure from the template and headers names")
                                    break
                                response = requests.post(url, headers=headers, data=body)
                                retrun_message_error(response)
                        except:
                            if 'From' in df.columns and 'To' in df.columns:
                                st.error(f"Please check the date format, Should be (Year-Month-day)")
                            else:
                                st.error(f"Please Make sure from the template and headers names")
                    
                
                    #st.info('We are still working on this module', icon="ℹ️")
                    
            elif option == "Supplements":
            
                col1, col2, col3, col4,col5 = st.columns(5)
                with col1:
                    supplement_Types = st.selectbox("What is The Supplement Type?",("Basic"),)#, "ShortStay"
                    
                with col2:
                    price_For = st.selectbox("Price For?",("Room", "Price per person"),)
                
                with col3:
                    active = st.selectbox("Active?",("true", "false"),)
                
                with col4:
                    mandatory = st.selectbox("Mandatory?",("true", "false"),)
                    
                with col5:
                    base_supplement = st.selectbox("Base supplement?",("Fixed price", "Percentage"),)
                    
                col6, col7 = st.columns(2)
                
                with col6:
                    application_Types = st.selectbox("What is The Application Types?",("BasePrice", "BaseMeal","Total","TotalNoBaseRate"),)
                    
                with col7:
                    supplement_name = st.text_input("Enter the supplement name",placeholder="Supplement Name")
                
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                weekDays = []   
                days_options = st.multiselect("Choose the days?",["All","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],default=["All"],)
                if "All" in days_options:
                    weekDays.append("X"*7)
                else:
                    for d in days:
                        if d in days_options:
                            weekDays.append("X")
                        else:
                            weekDays.append("-")
                weekDays = "".join(weekDays)
                #st.write(weekDays)
                    
                if st.button(f"Upload {option}",use_container_width=True,type="primary"):
                    df = pd.read_excel(uploaded_file)
                    try:
                        df['From'] = df['From'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        df['To'] = df['To'].apply(lambda x : x.strftime("%Y-%m-%d"))
                        for i,row in df.iterrows():
                            try:
                                if price_For == "Room" and supplement_Types == "Basic":
                                    x = upload_basic_supplement_per_room(row,supplement_Types,application_Types,supplement_name,price_For,active,mandatory,base_supplement,weekDays)
                                elif price_For == "Room" and supplement_Types == "ShortStay":
                                    x = upload_basic_supplement_per_shortstay(row,supplement_Types,application_Types,supplement_name,price_For,active,mandatory,base_supplement,weekDays)
                                elif price_For == "Price per person" and supplement_Types == "Basic":
                                    x = upload_basic_supplement_per_person(row,supplement_Types,application_Types,supplement_name,price_For,active,mandatory,base_supplement,weekDays)
                                else:
                                    st.info('We are still working on this module', icon="ℹ️")
                                    break
                            except:
                                st.error(f"Please Make sure from the template and headers names")
                                break
                            body = build_body(x)
                            #st.write(body)
                            response = requests.post(url, headers=headers, data=body)
                            retrun_message_error(response)
                    except:
                        if 'From' in df.columns and 'To' in df.columns:
                            st.error(f"Please check the date format, Should be (Year-Month-day)")
                        else:
                            st.error(f"Please Make sure from the template and headers names")

            
st.write("Developed By: **Eng. Amr Atef** ⌨️")