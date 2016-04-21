from flask import Flask,render_template,request,jsonify
from flask_restful import Resource ,Api
from algorithm import start
app=Flask(__name__)
api=Api(app)


@app.route('/')
def home():
    return render_template('tictactoe.html')
class Moves(Resource):
    def post(self):
        val=request.json
        board=val['move']
        print board
        move=start(1,board)
        data={'move':move['move'],'status':move['status']}
        return  data
    def get(self):
        return "Moves"

class getPlayer(Resource):
	def post(self):
		val=request.json
		print val
		return val['player']
		data={'val':val['player']}
		return jsonify(data=data)
	def get(self):
		return "Player"

api.add_resource(Moves,'/moves')
api.add_resource(getPlayer,'/player')



if __name__=='__main__':
    app.run(debug=True)


