import sqlite3, string

def CreateDB():
    _dbConn = sqlite3.connect('database.db')
    _cursor = _dbConn.cursor()
    
    # drop the options table if it exists
    _cursor.execute("DROP TABLE IF EXISTS Options")
    
    # recreate table
    _tableToCreate = """ CREATE TABLE Options (
            Name CHAR(50) NOT NULL,
            Desc CHAR(255) NOT NULL,
            NumbOfChars INT (3),
            LCase BOOL NOT NULL,
            UCase BOOL NOT NULL,
            Numb BOOL NOT NULL,
            Special BOOL NOT NULL,
            ExcludeAmbiguous BOOL NOT NULL
        ); """
    
    _cursor.execute(_tableToCreate)
    
    # insert data into Options table
    _cursor.execute('''INSERT INTO Options VALUES ('Memerable', 'Perfect for securing your computer or mobile device, or somewhere brute force is detectable.', '10', 1, 1, 1, 0, 0)''')
    _cursor.execute('''INSERT INTO Options VALUES ('Lower Case Only', 'Generates 8 character lower case only random strings.', '8', 1, 0, 0, 0, 0)''')
    _cursor.execute('''INSERT INTO Options VALUES ('Upper Case Only', 'Generates 8 character upper case only random strings.', '8', 0, 1, 0, 0, 0)''')
    _cursor.execute('''INSERT INTO Options VALUES ('Strong', 'Generates 10 character random strings with upper and lower case numbers and special characters.', '10', 1, 1, 1, 1, 0)''')
    _cursor.execute('''INSERT INTO Options VALUES ('Fortknox', 'Generates 20 character random strings with upper and lower case numbers and special characters.', '20', 1, 1, 1, 1, 0)''')
    
    
    # save changes to database table
    _dbConn.commit()
    
    # close database connections
    _cursor.close()
    _dbConn.close()
 
# run CreateDB function to initialize database and create and insert data for the Options table   
#CreateDB()

def GetListOfNamesOfOptions():
    _dbConn = sqlite3.connect('database.db')
    _cursor = _dbConn.cursor()
    
    _list = _cursor.execute('''SELECT Name FROM Options''')
    
    return _list

#_listOfOptionNames = GetListOfNamesOfOptions()


for _name in _listOfOptionNames:
    print('Found option: {}'.format(_name))
    
    if "Lower Case Only" in _name:
        print("option chosen is LowerCase Only")
    else:
        print("option chose is not LowerCase Only")

# Search Database for number of characters
def SearchDataBase(_tableName, _columnNeeded, _columnToSearch, _valueToFind):
    _dbConn = sqlite3.connect('database.db')
    _cursor = _dbConn.cursor()
    
    _query = "SELECT {} FROM {} WHERE {} LIKE '{}'".format(_columnNeeded, _tableName, _columnToSearch, _valueToFind)
    
    _result = [ x[0] for x in _cursor.execute(_query).fetchall() ]
    
    return _result[0]

#print("I got: '{}'".format(SearchDataBase("Options", "Desc", "Name", "Fortknox")))

def CountDown(_iterationsToMake):
    i = 1
    while int(_iterationsToMake) >=i:
        print("This is the {} iteration!".format(i))
        i += 1
    
#CountDown(SearchDataBase("Options", "NumbOfChars", "Name", "Fortknox"))
