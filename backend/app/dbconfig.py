class DbConfig:
   _dbHost:str = '192.168.0.202'
   _dbPort:str = '5432'
   _dbName:str = 'pos_bakery'
   _dbUser:str = 'postgres'
   _dbPassword:str = '123456'
   def __init__(self):
      pass
   """
   def __init__(dbHost, dbPort, dbName, dbUser, dbPassword):
      _dbHost = dbHost
      _dbPort = dbPort
      _dbName = dbName
      _dbUser = dbUser
      _dbPassword = dbPassword
    """
    
   def getHost(self) ->str:
      return self._dbHost
   def getPort(self) ->str:
      return self._dbPort
   def getName(self) ->str:
      return self._dbName
   def getUser(self) ->str:
      return self._dbUser
   def getPassword(self) ->str:
      return self._dbPassword
      
      






      
      
