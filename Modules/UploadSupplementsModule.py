import numpy as np

def upload_basic_supplement_per_room(row, supplementtype, applicationtype, supplementname, pricefor, active, mandatory,baseSupplement,weekdays):
    
    if baseSupplement == "Percentage":
        baseSupplement = "Percent"
    else:
        baseSupplement = "Room"
    
    if np.isnan(row['BoardCode']) and np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    <{baseSupplement} Amount = "{row['Amount']}"/>
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
    
    elif np.isnan(row['BoardCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <RoomTypes>
                                <RoomType Code = "{int(row['RoomCode'])}"/>
                            </RoomTypes>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    <{baseSupplement} Amount = "{row['Amount']}"/>
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
    
    elif np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    <{baseSupplement} Amount = "{row['Amount']}"/>
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
   
    else:
        x = f"""
        <Contracts>
            <Contract Code = "{row['ContractCode']}">
                <Supplements>
                    <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                        <Boards>
                            <Board Code = "{int(row['BoardCode'])}"/>
                        </Boards>
                        <Names>
                            <Name Language = "es">{supplementname}</Name>
                            <Name Language = "en">{supplementname}</Name>
                        </Names>
                        <ApplicationDays WeekDays = "{weekdays}"/>
                        <Prices>
                            <Price Type = "Cost">
                                <{baseSupplement} Amount = "{row['Amount']}"/>
                            </Price>
                        </Prices>
                    </Supplement>
                </Supplements>
            </Contract>
        </Contracts>
        """
    return x



def upload_basic_supplement_per_shortstay(row, supplementtype, applicationtype, supplementname, pricefor, active, mandatory,baseSupplement,weekdays):
    
    if baseSupplement == "Percentage":
        baseSupplement = "Percent"
    else:
        baseSupplement = "Room"
    
    if np.isnan(row['BoardCode']) and np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <LengthOfStay MaxNights = "{row['Nights']}"/>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    <{baseSupplement} Amount = "{row['Amount']}"/>
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
    
    elif np.isnan(row['BoardCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <LengthOfStay MaxNights = "{row['Nights']}"/>
                            <RoomTypes>
                                <RoomType Code = "{int(row['RoomCode'])}"/>
                            </RoomTypes>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    <{baseSupplement} Amount = "{row['Amount']}"/>
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
    
    elif np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <LengthOfStay MaxNights = "{row['Nights']}"/>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    <{baseSupplement} Amount = "{row['Amount']}"/>
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
   
    else:
        x = f"""
        <Contracts>
            <Contract Code = "{row['ContractCode']}">
                <Supplements>
                    <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <LengthOfStay MaxNights = "{row['Nights']}"/>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                        <Boards>
                            <Board Code = "{int(row['BoardCode'])}"/>
                        </Boards>
                        <Names>
                            <Name Language = "es">{supplementname}</Name>
                            <Name Language = "en">{supplementname}</Name>
                        </Names>
                        <ApplicationDays WeekDays = "{weekdays}"/>
                        <Prices>
                            <Price Type = "Cost">
                                <{baseSupplement} Amount = "{row['Amount']}"/>
                            </Price>
                        </Prices>
                    </Supplement>
                </Supplements>
            </Contract>
        </Contracts>
        """
    return x
    
    

def upload_basic_supplement_per_person(row, supplementtype, applicationtype, supplementname, pricefor, active, mandatory,baseSupplement,weekdays):
    
    if baseSupplement == "Percentage":
        baseSupplement = "Percent"
    else:
        baseSupplement = "Room"
    adult = ""
    addi_adult = ""
    childA = ""
    childB = ""

    
    if np.isnan(row['adu']) == False:
        adult = f"""<Adult Amount = "{row['adu']}"/>"""
    if np.isnan(row['adi']) == False:
        addi_adult = f"""<AdultAdditionals>
                            <AdultAdditional Amount = "{row['adi']}" Order = "1"/>
                        </AdultAdditionals>"""
    if np.isnan(row['chA1']) == False and np.isnan(row['chA2']) == False:
        childA = f"""<ChildrenA>
                        <ChildA Amount = "{row['chA1']}" Order="1"/>
                        <ChildA Amount = "{row['chA2']}" Order="2"/>
                    </ChildrenA>"""
    elif np.isnan(row['chA1']) == False:
        childA = f"""<ChildrenA>
                        <ChildA Amount = "{row['chA1']}" Order="1"/>
                    </ChildrenA>"""
    elif np.isnan(row['chA2']) == False:
        childA = f"""<ChildrenA>
                        <ChildA Amount = "{row['chA2']}" Order="2"/>
                    </ChildrenA>"""
                    
    if np.isnan(row['chB1']) == False and np.isnan(row['chB2']) == False:
        childB = f"""<ChildrenB>
                        <ChildB Amount = "{row['chB1']}" Order="1"/>
                        <ChildB Amount = "{row['chB2']}" Order="2"/>
                    </ChildrenB>"""
                    
    elif np.isnan(row['chB1']) == False:
        childB = f"""<ChildrenB>
                        <ChildB Amount = "{row['chB1']}" Order="1"/>
                    </ChildrenB>"""
    elif np.isnan(row['chB2']) == False:
        childB = f"""<ChildrenB>
                        <ChildB Amount = "{row['chB2']}" Order="2"/>
                    </ChildrenB>"""
    
    if np.isnan(row['BoardCode']) and np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    {adult}
                                    {addi_adult}
                                    {childA}
                                    {childB}
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
    
    elif np.isnan(row['BoardCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <RoomTypes>
                                <RoomType Code = "{int(row['RoomCode'])}"/>
                            </RoomTypes>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    {adult}
                                    {addi_adult}
                                    {childA}
                                    {childB}
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
    
    elif np.isnan(row['RoomCode']):
        x = f"""
            <Contracts>
                <Contract Code = "{row['ContractCode']}">
                    <Supplements>
                        <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                            <Dates>
                                <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Boards>
                                <Board Code = "{int(row['BoardCode'])}"/>
                            </Boards>
                            <Names>
                                <Name Language = "es">{supplementname}</Name>
                                <Name Language = "en">{supplementname}</Name>
                            </Names>
                            <ApplicationDays WeekDays = "{weekdays}"/>
                            <Prices>
                                <Price Type = "Cost">
                                    {adult}
                                    {addi_adult}
                                    {childA}
                                    {childB}
                                </Price>
                            </Prices>
                        </Supplement>
                    </Supplements>
                </Contract>
            </Contracts>
            """
   
    else:
        x = f"""
        <Contracts>
            <Contract Code = "{row['ContractCode']}">
                <Supplements>
                    <Supplement Type = "{supplementtype}" Active = "{active}" AplicationType = "{applicationtype}" Mandatory = "{mandatory}">
                        <Dates>
                            <Date From = "{row['From']}" To = "{row['To']}"/>
                        </Dates>
                        <RoomTypes>
                            <RoomType Code = "{int(row['RoomCode'])}"/>
                        </RoomTypes>
                        <Boards>
                            <Board Code = "{int(row['BoardCode'])}"/>
                        </Boards>
                        <Names>
                            <Name Language = "es">{supplementname}</Name>
                            <Name Language = "en">{supplementname}</Name>
                        </Names>
                        <ApplicationDays WeekDays = "{weekdays}"/>
                        <Prices>
                            <Price Type = "Cost">
                                {adult}
                                {addi_adult}
                                {childA}
                                {childB}
                            </Price>
                        </Prices>
                    </Supplement>
                </Supplements>
            </Contract>
        </Contracts>
        """
    return x