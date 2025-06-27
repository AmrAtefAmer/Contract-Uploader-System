import numpy as np
def upload_rates(row):
    if np.isnan(row['ChildA']):
        ChildA = 0
    else:
        ChildA = row['ChildA']
        
    if np.isnan(row['ChildB']):
        ChildB = 0
    else:
        ChildB = row['ChildB']
    if np.isnan(row['ExtraAdult']):
        x = f"""<Contracts>
          <Contract Code = "{row['ContractCode']}">
                <Rates>
                      <Rate Type = "Fixed">
                            <Dates>
                                  <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Prices>
                                  <Price RoomTypeCode = "{int(row['RoomCode'])}" BoardCode = "{int(row['BoardCode'])}" Type = "Cost">
                                  <Room Amount = "{row['Rate']}"/>
                                        <ChildrenA>
                                              <ChildA Amount = "{ChildA}" Order = "1"/>
                                        </ChildrenA>
                                        <ChildrenB>
                                              <ChildB Amount = "{ChildB}" Order = "1"/>
                                        </ChildrenB>
                                  </Price>
                            </Prices>
                      </Rate>
                </Rates> 
          </Contract>
        </Contracts>"""
        return x
    elif np.isnan(row['ExtraAdult']) == False:
        x = f"""<Contracts>
          <Contract Code = "{row['ContractCode']}">
                <Rates>
                      <Rate Type = "Fixed">
                            <Dates>
                                  <Date From = "{row['From']}" To = "{row['To']}"/>
                            </Dates>
                            <Prices>
                                  <Price RoomTypeCode = "{int(row['RoomCode'])}" BoardCode = "{int(row['BoardCode'])}" Type = "Cost">
                                  <Room Amount = "{row['Rate']}"/>
                                      <AdultAdditionals>
                                          <AdultAdditional Amount = "{row['ExtraAdult']}" Order = "1"/>
                                      </AdultAdditionals>
                                        <ChildrenA>
                                              <ChildA Amount = "{ChildA}" Order = "1"/>
                                        </ChildrenA>
                                        <ChildrenB>
                                              <ChildB Amount = "{ChildB}" Order = "1"/>
                                        </ChildrenB>
                                  </Price>
                            </Prices>
                      </Rate>
                </Rates> 
          </Contract>
        </Contracts>"""
        return x