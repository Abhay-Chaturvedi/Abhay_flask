from flask import Flask, request, render_template, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>My first Flask homeage</h1>"

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=="GET":
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        avg_marks=(maths+science+history)/3
        """ if avg_marks>50:
            result1="passed"
        else:
            result1="fail"
        return redirect(url_for(result1,score=avg_marks))
        """
        return render_template('result.html',avg_marks=avg_marks)
    
@app.route('/fail/<int:score>')
def fail(score):
    return 'Person is failed to clear exam, try again. Marks obtained:' + str(score)

@app.route('/passed/<int:score>')
def passed(score):
    return 'Person is passed. Marks obtained:' + str(score)

        

if __name__ == "__main__":
    app.run(debug=True)