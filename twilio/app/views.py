from flask import request, redirect, make_response
from app import app
from datetime import datetime, timedelta
import twilio.twiml
import sqlite3
from twilio.rest import TwilioRestClient

account_sid = "AC5db2f903ee4a9ad48869db297e2a8acd"
auth_token = "868a8ae2f1377d3a421c2d7237d52fdc"

client = TwilioRestClient(account_sid, auth_token)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    body = request.values.get('Body', None)

    from_number = request.values.get('From')

    resp = twilio.twiml.Response()

    messages = client.messages.list(
        from_=from_number
    )
    message = "You said " + messages[0].body

    labor_id = 0

    last_message = (messages[1].body).encode('ascii','ignore')
    current_message = (messages[0].body).encode('ascii','ignore')
    if current_message == "1" or current_message == "2" or current_message == "3":
        if current_message == "1":
            resp.message("\nYardwork Great! An employer will contact you if there is a match!")
            skill_id = "Yardwork"
        elif current_message == "2":
            resp.message("\nConstruction Great! An employer will contact you if there is a match!")
            skill_id = "Construction"
        elif current_message == "3":
            resp.message("\nPainting Great! An employer will contact you if there is a match!")
            skill_id = "Painting"

        conn = sqlite3.connect('/Users/parv/Desktop/l2d_iolab/Labor2Day_2.0/app.db')
        print "Opened database successfully";
        cursor = conn.execute("SELECT * from laborer")
        x = len(cursor.fetchall())
        labor_id = x + 1
        availability = 'y'

        conn.execute("INSERT INTO laborer VALUES (?,?,?,?,?)", (labor_id,last_message,from_number,availability,skill_id))

        print "Operation done successfully";
        conn.commit()
        conn.close()

    elif current_message.lower() == "yes" or current_message.lower() == "no":
      conn = sqlite3.connect('/Users/parv/Desktop/l2d_iolab/Labor2Day_2.0/app.db')
      check_number = from_number.lstrip('+')
      last_name = (messages[2].body).encode('ascii','ignore')
      curs = conn.execute("SELECT laborer_id From laborer where laborer_phone_num = ? and laborer_name = ?",(check_number,last_name))
      for row in curs:
        id_value = row[0]
      if current_message.lower() == 'yes':

        print last_name

        print check_number



        conn.execute("UPDATE fulfillment SET fulfillment_status= 'active' WHERE fulfillment_laborer_id = ?",(id_value,))
        conn.commit()
        conn.close()

      if current_message.lower() == "no":
        conn.execute("DELETE from fulfillment where fulfillment_laborer_id = ?",(id_value,))
        conn.execute("UPDATE laborer SET laborer_availability = 'y' WHERE laborer_id = ?",(id_value,))
        conn.commit()
        conn.close()



    else:
        resp.message("\nHello " + current_message + "\n Welcome to Labor2Day \n" + "Press 1 for Yardwork \n" + "Press 2 for Construction \n" + "Press 3 for Painting \n")

    return str(resp)
