#!/usr/bin/env python3
# Written by: Abhigyan Kumar
# Created on: 09/Nov/2022
# Modified on: 09/Nov/2022

from flask import Flask, request, render_template


app = Flask("Flask Arithmetic WebApp")  # The name of the Flask app created.
valid_values = ["add","subtract","multiply","divide"]  # Use for form validation.

def add(values = []):
	return values[0] + values[1]

def subtract(values = []):
	return values[0] - values[1]

def multiply(values = []):
	return values[0] * values[1]

def divide(values = []):
	return "Quotient: " + str(values[0] // values[1]) + " Remainder: " + str(values[0] % values[1])
	## You can do it simply with values[0] / values[1] too if you want a single output string

def db_writer(result):  # Complete it in a modular fashion.
	pass

@app.route("/")  # The base URL.
def home_page():
	return render_template("home.html")

@app.route("/result", methods=["POST"])  # Not allowing GET request as it's not an expected usecase.(u can however support it and redirect to / page)
def result_page():
	# print(request.form,type(request.form))
	#  Harvest the values.
	val1 = request.form.get("value1")
	val2 = request.form.get("value2")
	operation = request.form.get("operation")
	#  Validate the values.
	try:
		val1 = int(val1)
	except:
		raise ValueError("Invalid Value1 Received!!!")  # Check if user input is valid. (NEVER TRUST USER INPUTs)
	
	try:
		val2 = int(val2)
	except:
		raise ValueError("Invalid Value2 Received!!!")  # Check if user input is valid. (NEVER TRUST USER INPUTs)

	if operation not in valid_values:  # Check if user input is valid. (NEVER TRUST USER INPUTs)
		raise ValueError("Invalid Operation Selected!!!")
	
	#  Perform the calculaton.
	if operation == "add":  #  You can also use switch / case to do this.
		result = add([val1,val2])
		return render_template("result.html",result = result)

	elif operation == "subtract":
		result = subtract([val1,val2])
		return render_template("result.html",result = result)

	elif operation == "multiply":
		result = multiply([val1,val2])
		return render_template("result.html",result = result)

	elif operation == "divide":
		result = divide([val1,val2])
		return render_template("result.html",result = result)



app.run(host="0.0.0.0",port="8000",debug=False)  # 0.0.0.0 to RUN ON ALL localports (i.e. 127.0.0.1 is included)