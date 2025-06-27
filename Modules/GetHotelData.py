import pandas as pd
import requests
import xmltodict

juniper_user = 'xxxxxxxxxxx'
juniper_password = 'xxxxxxxxxxxx'

def return_hoteldata(hotelcode):

    url="xxxxxxxxxxxxxxxxxxxxx"
    headers = {'content-type': 'text/xml','SOAPAction':'http://www.juniper.es/webservice/2007/xxxxxxxxxxx',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"}
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <HotelDetail xmlns="http://www.juniper.es/webservice/2007/">
          <HotelDetailRQ Version="1" Language="ES">
          <Login Email="{juniper_user}" Password="{juniper_password}"/>
            <HotelDetailRequest>
              <Hotel Code="{hotelcode}"/>
            </HotelDetailRequest>
          </HotelDetailRQ>
        </HotelDetail>
      </soap:Body>
    </soap:Envelope>"""
    reponse = requests.post(url, headers=headers, data=body)
    data = xmltodict.parse(reponse.text)
    
    hotelName = data['soap:Envelope']['soap:Body']['HotelDetailResponse']['HotelDetailRS']['HotelDetailResponse']['Hotel']['Names']['Name'][0]['#text']
    rooms = data['soap:Envelope']['soap:Body']['HotelDetailResponse']['HotelDetailRS']['HotelDetailResponse']['Hotel']['RoomTypes']['RoomType']
    
    df = pd.DataFrame(columns=['Hotel Name','Room Code','Room Name'])
    for r in rooms:
        #print(r['@Code'], r['Names']['Name'][0]['#text'])
        row = [hotelName, r['@Code'], r['Names']['Name'][0]['#text']]
        df.loc[len(df)] = row
    
    return df
    
def return_hotelcontracts(hotelcode):

    url="https://www.eetglobal.com/webservicejpdm/operations/hotelextranettransactions.asmx"
    headers = {'content-type': 'text/xml','SOAPAction':'http://www.juniper.es/webservice/2007/HotelExtranetContractList',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"}
    body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns="http://www.juniper.es/webservice/2007/">
        <soapenv:Header/>
            <soapenv:Body>
                <HotelExtranetContractList>
                    <HotelExtranetContractListRQ Version="1" Language="es">
                        <Login Email="{juniper_user}" Password="{juniper_password}"/>
                        <HotelExtranetContractListRequest IncludeExpired="false">
                            <Hotels>
                                <Hotel Code="{hotelcode}"/>
                            </Hotels>
                        </HotelExtranetContractListRequest>
                    </HotelExtranetContractListRQ>
                </HotelExtranetContractList>
            </soapenv:Body>
    </soapenv:Envelope>"""
    response = requests.post(url, headers=headers, data=body)
    data = xmltodict.parse(response.text)
    
    contracts = data['soap:Envelope']['soap:Body']['HotelExtranetContractListResponse']['HotelExtranetContractListRS']['Hotels']['Hotel']['Contracts']['Contract']
    
    df2 = pd.DataFrame(columns=['Contract Code','Active/Not','Contract Name','From', 'To'])
    if isinstance(contracts,list):
        for c in contracts:
            row = [c['@Code'], c['@Active'], c['Name'], c['Season']['@From'], c['Season']['@To']]
            df2.loc[len(df2)] = row
    else:
        row = [contracts['@Code'], contracts['@Active'], contracts['Name'], contracts['Season']['@From'], contracts['Season']['@To']]
        df2.loc[len(df2)] = row
    return df2
