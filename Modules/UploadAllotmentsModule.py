import numpy as np
def upload_allotments(row):

    if isinstance(row['Allotments'], str) and row['Allotments'].lower() == 'fs':

        x = f"""<Contracts>
                  <Contract Code = "{row['ContractCode']}">
                        <Allotments>
                            <Allotment FreeSales = "true">
                                    <Dates> <Date From = "{row['From']}" To = "{row['To']}"/> </Dates>
                                    <RoomTypes> <RoomType Code = "{int(row['RoomCode'])}"/> </RoomTypes>
                            </Allotment>
                        </Allotments>
                  </Contract>
            </Contracts>"""
    else:
        x = f"""<Contracts>
                  <Contract Code = "{row['ContractCode']}">
                        <Allotments>
                            <Allotment BaseAllotment = "{row['Allotments']}" FreeSales = "false">
                                    <Dates> <Date From = "{row['From']}" To = "{row['To']}"/> </Dates>
                                    <RoomTypes> <RoomType Code = "{int(row['RoomCode'])}"/> </RoomTypes>
                            </Allotment>
                        </Allotments>
                  </Contract>
            </Contracts>"""
    return x