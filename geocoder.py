# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 00:54:51 2020

@author: Sayantan
"""

from flask import Flask, render_template, request, send_file
from modify_data import *
from werkzeug import secure_filename

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST','GET'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        try:
            output=modify_data(file)
            output.to_csv("modified_"+file.filename)
            return render_template("index.html", tables=[output.to_html(classes='data',header="true")], btn="download.html")
        except KeyError:
            return render_template("index.html",text="Your file doesn't contain a field named Address")
        except:
            return render_template("index.html",geocoder="Timeout Error")
              
@app.route("/download")
def download():
    return send_file("modified_"+file.filename, attachment_filename="GeoData.csv", as_attachment=True)
       
if __name__=='__main__':
    app.run()
    
