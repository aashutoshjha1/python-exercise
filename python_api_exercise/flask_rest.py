#!/usr/bin/env python3

import site
site.addsitedir("/Users/a0j0b83/.pyenv/versions/3.7.12/lib/python3.7/site-packages")

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# Create name app

app = Flask(__name__)

# App object

api = Api(app)

class greeting(Resource):
      def get(self):

            return jsonify({'message': 'hello world'})

      def post(self):
          data = request.get_json()
          return jsonify({'data': data}), 201

class Square(Resource):
      
      def get(self, num):
           return jsonify({'square': num**2})
    
      def post(self):
         square = num*num
         return jsonify({'data': square})
       
      

api.add_resource(greeting, '/')
api.add_resource(Square, '/square/<int:num>')

if __name__ == '__main__':
    app.run(debug = True)


          

