from flask import Flask,redirect,url_for, render_template,request


app =Flask(__name__)

@app.route("/")
def welcomefunction():
    return render_template('form.html')


@app.route("/success/<int:score>")
def successfunction(score):
    return "The person has scored "+str(score)+ "and Passed"

@app.route("/fail/<int:score>")
def failfunction(score):
    return "The person has scored "+str(score)+ " and Failed"

@app.route("/result/<int:marks>")
def Resultchecker(marks):
    result1=""
    if marks>50:
        result1='successfunction'
    else:
        result1='failfunction'
    
    #return redirect(url_for(result, score = marks))
    return render_template('result.html',result=result1)

@app.route("/index",methods=['POST'])
def Resultchecker1():
    result=""
    marks=(float(request.form['maths'])+float(request.form['science'])+float(request.form['history']))/3
    if marks>50:
        result='successfunction'
    else:
        result='failfunction'
    
    return redirect(url_for(result, score = marks))
    

if __name__ == '__main__':
    app.run(debug=True)
