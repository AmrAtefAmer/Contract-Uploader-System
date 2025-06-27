def upload_stopsales(row,action):
    x = f"""<Contracts>
            <Contract Code = "{row['ContractCode']}">
                <StopSales>
                    <StopSale Action = "{action}">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                    </StopSale>
                </StopSales>
            </Contract>
        </Contracts>"""
    return x