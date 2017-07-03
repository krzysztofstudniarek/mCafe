import flask

from flask import Flask
from flask import request
from flask import render_template


class Machine:
    def __init__(self, id, name):
        self.id = id
        self.status = False
        self.name = name

app = Flask(__name__)

machines = []

@app.route('/')
def hello_world():
    return render_template('index.html', machines = machines)

@app.route('/update', methods=['GET'])
def update():
   global status 

   for i in range(len(machines)):
       if reques.args.get('id') == machines[i].id :
           machines[i].status = request.args.get('status') == 'true'
           break

   return 'STATUS UPDATED'
if __name__ == '__main__':
   #app.run("192.168.43.246")
   machines.append(Machine('32e5e5ca-d02b-4d65-9024-6b724183ca52', '4 pietro'))
   machines.append(Machine('7d721220-6b53-436c-919f-870ab0622d7e', 'Hackathon'))
   app.run(debug=True)
