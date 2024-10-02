from flask import Flask,redirect,render_template,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import csv
import os

#  =================== app configurations ===================

app=Flask(__name__)
csv_file_path='data.csv'
# =========== models =================


# ============= route ================

@app.route("/")
def index():   
    try:
        return render_template("dashoard.html")
    except Exception as e:
        return f"error {e}"

@app.route("/datasend",methods=['POST'])
def datasend():
    try:
        numbers = request.form.getlist('num')
        
        number_list = []
        for num in numbers:
            if num.strip(): 
                try:
                    number_list.append(int(num))
                except ValueError:
                    return f"Invalid input: {num} is not a number.", 400
        print(number_list)
        if not number_list:
            return "No numbers provided.", 400

        sorting = request.form.get('sorting')
        if not sorting:
            return "No sorting algorithm selected.", 400

        if sorting=="BS":
            new_sorting="Booble Sort"
        elif sorting=="SS":
            new_sorting="Selection Sort"
        elif sorting=="IS":
            new_sorting="Insertion Sort"
        elif sorting=="QS":
            new_sorting="Quik Sort"
        elif sorting=="MS":
            new_sorting="Marge Sort"
        
        sort_list = sorted(number_list)

        print(f"Sorted List: {sort_list}")

        return render_template("dashoard.html", data=sort_list, sorting=new_sorting)  # Ensure template name is correct

    except Exception as e:
        # Log the exception details
        print(f"Error: {e}")
        return "An error occurred while processing your request.", 500

# ================ app run ===============
