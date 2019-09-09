# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect,make_response

from werkzeug import secure_filename
import helpers
import extracttable as et
app=Flask(__name__)

@app.route("/")
def upload_home():
    return render_template("upload.html")

@app.route('/upload',methods=["POST"])
def upload_file_output():
    if "file" not in request.files:
        return "No user in request.files"
    file=request.files["file"]
    if file.filename=="":
        return "Please select the file"
    if file :
        file.filename=secure_filename(file.filename)
        output=helpers.upload_file_s3(file,"textractpython")
        fils=[]
        for fil in output:
            fils.append(fil['Key'])
            
        
        return render_template("files.html",result=fils)
    else:
        return redirect('/')
    
@app.route('/result',methods=["POST"])      
def result_table():
    if request.method=="POST":
        select_val=request.form['containers']
        response=et.connection_tables("textractpython",select_val)
        result=et.result_tables(response)
        #return render_template("results.html",result=result.to_html())
        response=make_response(result.to_csv())
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
        response.headers["Content-Type"] = "text/csv"
        return response
        
        
        
    
    


if __name__=="__main__":
    app.run()