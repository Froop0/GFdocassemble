#import pyodbc

class fetchdata:
    
    def __init__(self):
        # Connection to SQL DB
        
        # Trusted connection uses the system credentials. Might require to be modified?        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AderantCoreSql1;'
                      'Database=EXP_LIVE;'
                     'TRUSTED_CONNECTION=TRUE')
        
        self.cursor = self.conn.cursor()
        
    def client_info(self, KlientNummer = None):
        
        if KlientNummer == None:
            print("No client number")
            return None
        else:
            print("Fetching data for client number: ", KlientNummer)
            
            client_info = self.cursor.execute(f"""
            SELECT HA2.CLIENT_CODE, HA1.NAME_UNO, HA1.ADDRESS1, HA1.CITY, HA1.COUNTRY_CODE 
                FROM HBM_ADDRESS HA1 
                    LEFt JOIN HBM_CLIENT HA2 ON (HA2.NAME_UNO = HA1.NAME_UNO) 
                        WHERE HA2.CLIENT_CODE = {KlientNummer} """).fetchall()
            return client_info
        
        
    def case_info(self, sagsnummer = None):
    
        if sagsnummer == None:
            print("No casenumber")
            return None
        else:
            print("Case number: ", sagsnummer)
            
            case_info = self.cursor.execute(f"""
            SELECT HM1.MATTER_NUMBER, HM1.CLIENT_UNO, HC21.CLIENT_UNO, HC21.SECURITY_ID,
            HC21.CLIENT_NAME, HM1.SECURITY_ID, HM1.MATTER_NAME, HM1.CLIENT_CODE,
            HM1.MATTER_CODE, HM1.MATTER_UNO, HM1.STATUS_CODE, HSM22.STATUS_CODE,
            HSM22.STATUS_DESC FROM HBM_MATTER HM1
                LEFT OUTER JOIN HBM_CLIENT HC21 ON (HM1.CLIENT_UNO=HC21.CLIENT_UNO) 
                LEFT OUTER JOIN HBL_STATUS_MATT HSM22 ON (HM1.STATUS_CODE=HSM22.STATUS_CODE) 
                    WHERE ( ( HM1.MATTER_UNO<>0 ) AND ( HM1.CLIENT_CODE LIKE ('%%') )
                    AND (HM1.MATTER_NUMBER = {sagsnummer}))
                        ORDER BY HM1.CLIENT_CODE
                        """).fetchall()
            
            return case_info
            
    def empl_info(self, MANummer = None, ):
        if MANummer == None:
            print("No employee number")
            return None
        else:
            print("Employee number: ", MANummer)
            
            empl_info = self.cursor.execute(f"""
                            SELECT HP1.INACTIVE, HP1.LOGIN, HP1.PROF, HP1.DEPT, HP1.OFFC,HP1.EMPLOYEE_NAME,
                            HP1.EMPLOYEE_CODE, HP1.INTERNAL_NUM FROM HBM_PERSNL HP1
                                WHERE ( ( HP1.INTERNAL_NUM = {MANummer} AND HP1.INACTIVE != 'Y' ) )
                                    ORDER BY HP1.EMPLOYEE_CODE
                            """).fetchall()
            return empl_info

#print(fetchdata().case_info(sagsnummer = 819512))
#print(fetchdata().empl_info(MANummer = 1887, initials = 'FFA'))
#print(fetchdata().client_info(KlientNummer = 721378))
