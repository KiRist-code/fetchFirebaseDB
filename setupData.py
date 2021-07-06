import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class SetUp:
    def fetchDB():
        cred = credentials.Certificate('chat-547bd-firebase-adminsdk-p4h8k-0b22801376.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://chat-547bd-default-rtdb.firebaseio.com/chat'
        })

        database = db.reference().get()
        print("Successfully Fetched")

        return database
    
    def fetchRoomKey(database,key):
        print("Fetched All Keys")
        return database[key].keys()

    def fetchDx(database,key,roomKey):
        print(database[key][roomKey].keys())
        print("Fetched All Dx")
        return database[key][roomKey]["dx"]

    def fetchUx(database,key,roomKey):
        print(database[key][roomKey].keys())
        print("Fetched All Ux")
        return database[key][roomKey]["ux"]

    def setTimestamp(dx,ux):
        if len(dx) > len(ux):
            timestamp = [0 for row in range(int(len(dx)))]
            print("dx!")
        else:
            timestamp = [0 for row in range(int(len(ux)))]
            print("ux!")

        for i in range(len(timestamp)):
            timestamp[i] = i

        print("Timestamp generated")
        return timestamp


class main:
    def main():
        f = open('data.csv','w',newline='')
        wr = csv.writer(f)

        checker = 0
        first_key = "chat"

        database = SetUp.fetchDB() #fetch DB
        datakeys = list(database["chat"].keys()) #fetch all keys list from DB
        print(datakeys)
        
        for i in range(len(datakeys)):
            secretKey = list(SetUp.fetchRoomKey(database=database[first_key],key=datakeys[i])) #fetch roomKey list from keys
            print(secretKey[0])

            dxlst = SetUp.fetchDx(database=database[first_key],key=datakeys[i],roomKey=secretKey[0])
            uxlst = SetUp.fetchUx(database=database[first_key],key=datakeys[i],roomKey=secretKey[0])
            timeStamp = SetUp.setTimestamp(dx=dxlst,ux=uxlst)

            timeStamp.insert(0,"list")
            timeStamp.append("person")
            header = timeStamp

            for p in range(2):
                if p % 2 == 0:
                    if checker == 0:
                        checker += 1
                        wr.writerow(header)

                    dxlst.insert(0,"dx-" + str(i))
                    dxlst.append(0)
                    wr.writerow(dxlst)
                else:
                    if checker == 1:
                        checker += 1
                        wr.writerow(header)

                    uxlst.insert(0,"ux-" + str(i))
                    dxlst.append(0)
                    wr.writerow(uxlst)

if __name__ == "__main__":
    main.main()

