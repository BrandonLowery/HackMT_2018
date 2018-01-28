import update_db


kom = update_db.database_update("kom") #creates a db_update object named kom


kom.add() #adds one to the count in the db for kom

x = kom.get_count() #gives you kom lot count

print(x)
k = kom.get_id()
print(k)

kom.sub()

x = kom.get_count()

print(x)
