import mysql.connector # or from mysql import connector
import requests

class Context:
    def __init__(self):
        self.con = mysql.connector
        
    def Connect(self):
        self.con.connect(
            host="den1.mysql3.gear.host",
            user="bancocangaco",
            password="Jn84kp4gZd-_",
            database="bancocangaco"
        )

    def Disconnect(self):
        self.con.close()