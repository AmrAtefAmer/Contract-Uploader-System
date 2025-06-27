import numpy as np

def upload_release(row):

    x = f"""
        <Contracts>
            <Contract Code = "{row['ContractCode']}">
                <Releases>
                    <Release Days = "{int(row['Release'])}">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                    </Release>
                </Releases>
            </Contract>
        </Contracts>"""
    return x
	
	
