from flask import Flask, render_template, request, url_for, redirect
from pwgen import gen_custom_pass

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def home0():
#        return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        length = int(request.form['length'])
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_special_chars = 'special' in request.form
        use_numbers = 'numbers' in request.form
        use_exclude = 'exclude' in request.form
        pword = gen_custom_pass(length, use_uppercase, use_lowercase, use_numbers, use_special_chars, use_exclude)
        return render_template('CustomPW.html', password=pword, 
        #return redirect(url_for('CustomPassGen', gen_pass=pword, 
                               length=length, 
                               lastUseUppercase=use_uppercase, 
                               lastUseLowercase=use_lowercase, 
                               lastUseSpecial=use_special_chars, 
                               lastUseNumbers=use_numbers, 
                               lastUseExclude=use_exclude) #)
    
    return render_template('CustomPW.html', lastUseUppercase=1,
                           lastUseLowercase=1,
                           lastUseSpecial=0,
                           lastUseNumbers=1,
                           lastUseExclude=0)

@app.route('/CustomPassGen')
def CustomPassGenerator(gen_pass, len, upper, lower, numb, spec, excl):
    return render_template('CustomPW.html', password=gen_pass, 
        default_length=len, 
        lastUseUppercase=upper, 
        lastUseLowercase=lower, 
        lastUseSpecial=spec, 
        lastUseNumbers=numb, 
        lastUseExclude=excl)

if __name__== '__main__':
    app.run(debug=True)
