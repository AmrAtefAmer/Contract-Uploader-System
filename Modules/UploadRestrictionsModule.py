import numpy as np

def upload_restriction_with_minstay(row):
    if np.isnan(row['BoardCode']) and np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "MinimumStay">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <LengthOfStay MinNights = "{row['MinimumStay']}"/>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x
    elif np.isnan(row['BoardCode']) and np.isnan(row['RoomCode'])== False:
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "MinimumStay">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <LengthOfStay MinNights = "{row['MinimumStay']}"/>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x
    
    elif np.isnan(row['RoomCode']) and np.isnan(row['BoardCode'])== False:
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "MinimumStay">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <LengthOfStay MinNights = "{row['MinimumStay']}"/>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x
        
    else:
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "MinimumStay">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <LengthOfStay MinNights = "{row['MinimumStay']}"/>
                            <RoomTypes>
                                <RoomType Code = "{int(row['RoomCode'])}"/>
                            </RoomTypes>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x

 
	
def upload_restriction_with_checkinorcheckout(row,restrictionType,weedays):
    if np.isnan(row['BoardCode']) and np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "{restrictionType}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <ApplicationDays WeekDays = "{weedays}"/>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x
    elif np.isnan(row['BoardCode']) and np.isnan(row['RoomCode'])== False:
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "{restrictionType}">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                        <ApplicationDays WeekDays = "{weedays}"/>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x
    
    elif np.isnan(row['RoomCode']) and np.isnan(row['BoardCode'])== False:
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "{restrictionType}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                            <ApplicationDays WeekDays = "{weedays}"/>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x
        
    else:
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Restrictions>
                        <Restriction Type = "{restrictionType}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <RoomTypes>
                                <RoomType Code = "{int(row['RoomCode'])}"/>
                            </RoomTypes>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                            <ApplicationDays WeekDays = "{weedays}"/>
                        </Restriction>
                    </Restrictions>
                </Contract>
            </Contracts>"""
        return x	
