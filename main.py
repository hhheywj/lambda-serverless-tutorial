import json
import psycopg2
import requests
import math

class Databases():
    def __init__(self):
        self.db = psycopg2.connect(host='DB',
                                   dbname='postgres', user='DB_USER', password='DB_PASSWORD', port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

class CRUD(Databases):
    def insertDB(self, schema, table, data1, data2):
        sql = " INSERT INTO {schema}.{table}(price, name) VALUES ('{data1}', '{data2}') ;".format(
            schema=schema, table=table, data1=data1, data2=data2)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" insert DB err ", e)

    def readDB(self, schema, table, colum):
        sql = " SELECT {colum} from {schema}.{table}".format(
            colum=colum, schema=schema, table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            result = (" read DB err", e)

        return result

    def updateDB(self, schema, table, colum, value, condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(
            schema=schema, table=table, colum=colum, value=value, condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" update DB err", e)

    def deleteDB(self, schema, table, condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(schema=schema, table=table,
                                                                          condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err", e)


def handler(event=None, context=None):
    db = CRUD()
    hook = 'https://hooks.slack.com/services/WORKSPACE/KEY'

    token_price = requests.get("TOKEN_PRICE_URL")
    token_result = json.loads(token_price.text)
    token_price_result = token_result.get("")
    db.insertDB(schema='public', table='TABLE_NAME', data1=token_price_result, data2='KLAY')
    requests.post(
        hook,
        headers={
            'content-type': 'application/json'
        },
        json={
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': "전송 TEXT"
                    }
                }
            ]
        }
    )
