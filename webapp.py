from flask import Flask, render_template, request, url_for, redirect
from pwgen import gen_custom_pass, predefined_pass
from db_stuff import *

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def home0():
#        return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def home():
    # grab list for drop down
    _dropdown1List = GetListOfNamesOfOptions()
    _paramLength = 14
    _paramLower = 1
    _paramUpper = 1
    _paramNumb = 1
    _paramSpecial = 1
    _paramExclude = 1

    if request.method == 'POST':

        use_optType = request.form.get('whatToGen')

        if use_optType == 'Memerable':
            _paramLength = 10
            _paramLower = 1
            _paramUpper = 1
            _paramNumb = 0
            _paramSpecial = 0
            _paramExclude = 0
        
        if use_optType == 'Strong':
            _paramLength = 14
            _paramLower = 1
            _paramUpper = 1
            _paramNumb = 1
            _paramSpecial = 1
            _paramExclude = 1

        if use_optType == 'FortKnox':
            _paramLength = 20
            _paramLower = 1
            _paramUpper = 1
            _paramNumb = 1
            _paramSpecial = 1
            _paramExclude = 0
        
        string01 = predefined_pass(use_optType)
        string02 = predefined_pass(use_optType)
        string03 = predefined_pass(use_optType)
        string04 = predefined_pass(use_optType)
        string05 = predefined_pass(use_optType)
        string06 = predefined_pass(use_optType)
        
        return render_template('index.html',
                               whatToGen=use_optType,
                               string01=string01,
                               string02=string02,
                               string03=string03,
                               string04=string04,
                               string05=string05,
                               string06=string06)

    use_optType = "Strong"
    
    string01 = predefined_pass(use_optType)
    string02 = predefined_pass(use_optType)
    string03 = predefined_pass(use_optType)
    string04 = predefined_pass(use_optType)
    string05 = predefined_pass(use_optType)
    string06 = predefined_pass(use_optType)
        
    return render_template('index.html',
                           whatToGen='Strong',
                           string01=string01,
                           string02=string02,
                           string03=string03,
                           string04=string04,
                           string05=string05,
                           string06=string06)


@app.route('/CustomPassGen', methods=['POST', 'GET'])
def CustomPass():
    if request.method == 'POST':
        length = int(request.form['length'])
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_special_chars = 'special' in request.form
        use_numbers = 'numbers' in request.form
        use_exclude = 'exclude' in request.form
        #use_optType = 'whatToGen' in request.form
        pword = gen_custom_pass(length, use_uppercase, use_lowercase, use_numbers, use_special_chars, use_exclude)
        #return render_template('index.html', password=pword, 
        return render_template('CustomPW.html',
                               password=pword, 
                               length=length, 
                               lastUseUppercase=use_uppercase, 
                               lastUseLowercase=use_lowercase, 
                               lastUseSpecial=use_special_chars, 
                               lastUseNumbers=use_numbers, 
                               lastUseExclude=use_exclude)
    return render_template('CustomPW.html',
                           lastUseUppercase=1,
                           lastUseLowercase=1,
                           lastUseSpecial=0,
                           lastUseNumbers=1,
                           lastUseExclude=0)
        



if __name__== '__main__':
    app.run(debug=True)
