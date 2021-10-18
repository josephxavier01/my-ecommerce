import sqlite3

db = sqlite3.connect("jorizonsupermarket.sqlite")
cur = db.cursor()
'''
query = cur.execute('drop table Visitors')
query = cur.execute('drop table Employee')
db.commit

query = cur.execute('CREATE  TABLE Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)')
query = cur.execute('CREATE  TABLE Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)')
db.commit()
'''

query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Obi', 'Franklin', '1', 'obi123', 'frankdnero', 'obifrank@gmail.com', '09078654565'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid,  UserName, Password,Email, PhoneNo)values(?,?,?,?,?,?,?)',('Garinu', 'Abubakar', '2', 'gareen01', 'garaba00', 'bubakar@yahoo.com', '07045432355'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Cooker', 'Adebanjo', '3', 'ban900', 'realcooker001', 'bcooker@gmail.com', '08036764289'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Bello', 'Adamu', '4', 'BelloAdam', 'hello002', 'debello@yahoo.com', '08145765467'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid,  UserName, Password,Email, PhoneNo)values(?,?,?,?,?,?,?)',('Odubulu', 'Wale', '5', 'bigwale', 'waleni22','bigwhale@gmail.com', '09035764345'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Obasanjo',  'Adesumi', '6','babasumi', 'sumsum', 'obasumi@gmail.com', '07096878555'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Oloye',  'Oliver', '7','oliveman', 'doochee', 'oliver@yahoo.com', '08056421387'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid, UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Adoo', 'Francisca', '8', 'ciscadoo', 'cisca2121', 'dofrances@gmail.com', '08056431134'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid,  UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Oforka', 'Barthlomew', '9',  'fornew', 'frrmm333', 'forka@gmail.com', '07067654346'))
query = cur.execute('INSERT into Employee(FirstName, LastName, Employeeid,  UserName, Password, Email, PhoneNo)values(?,?,?,?,?,?,?)',('Oghene', 'Maria', '10', 'mariene', 'mama123', 'mariene@yahoo.com', '09078644577'))

query = cur.execute('INSERT into Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Amina Lattifah', 'aminafah', 'mina44', 'No 2 Mutala Mohammed street', '49', '07078373732', 'lattif@gmail.com'))
query = cur.execute('INSERT into Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Abdulwaheed Adeniran', 'weeddo', 'niran', 'No 14 Adeleke close', '44', '07067432567', 'adeniran@gmail.com'))
query = cur.execute('INSERT into Visitors(Name, UserName, Password,  Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Okenna Vincent', 'Vindee', 'vean333', 'No 29 Adebanjo crescent', '65', '08056738273', 'banjo@yahoo.com'))
query = cur.execute('INSERT into Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Agana Respect', 'gainrespect', 'respect4', 'No 147 soweto street', '20', '08032232322', 'respectme@yahoo.com'))
query = cur.execute('INSERT into Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Okon Okon Ade', 'Okonde', 'okon333', 'No 76 Ibrahim Galadima street', '27', '07067564683', 'galama@gmail.com'))
query = cur.execute('INSERT into Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Zubby Michael', 'Mikedean', 'mike222', 'No 98 Ali ibn Muktarstreet', '33', '08045677655', 'realzeal@yahoo.com'))
query = cur.execute('INSERT into Visitors(Name, UserName, Password, Address, Age, PhoneNo, Email)values(?,?,?,?,?,?,?)',('Ajoke Paschal', 'Paschaline111', 'pas123', 'No 1 Obi Okoye street', '32', '09067656566', 'jokepaschal@gmail.com'))
db.commit()
