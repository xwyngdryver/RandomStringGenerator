from flask import Flask, render_template, request, url_for, redirect
from pwgen import gen_custom_pass, predefined_pass
from db_stuff import *

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def home0():
#        return render_template('index.html')

# Global Variables
# creating list of options
getDropDownOptions = GetListOfNamesOfOptions()
unCleanDropDownOptions = list(getDropDownOptions)
_dropdown1List = CleanTheList(unCleanDropDownOptions)

@app.route('/', methods=['POST', 'GET'])
def home():
    # grab list for drop down
    #_dropdown1List = CleanTheList(unCleanDropDownOptions)
    #_paramLength = 14
    #_paramLower = 1
    #_paramUpper = 1
    #_paramNumb = 1
    #_paramSpecial = 1
    #_paramExclude = 1
        

    if request.method == 'POST':

        use_optType = request.form.get('whatToGen')
        description = SearchDataBase("Options", "Desc", "Name", use_optType)
        description = SearchDataBase("Options", "Desc", "Name", use_optType)
        _length = SearchDataBase("Options", "NumbOfChars", "Name", use_optType)
        _useUpper = SearchDataBase("Options", "UCase", "Name", use_optType)
        _useLower = SearchDataBase("Options", "LCase", "Name", use_optType)
        _useNumber = SearchDataBase("Options", "Numb", "Name", use_optType)
        _useSpecial = SearchDataBase("Options", "Special", "Name", use_optType)
        _excludeAmbiguous = SearchDataBase("Options", "ExcludeAmbiguous", "Name", use_optType)
    
    
        string01 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        string02 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        string03 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        string04 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        string05 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        string06 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        return render_template('index.html',
                               # HTML_jinja_var=_python_var
                               _dropdown1List=_dropdown1List,
                               whatToGen=use_optType,
                               _description=description,
                               string01=string01,
                               string02=string02,
                               string03=string03,
                               string04=string04,
                               string05=string05,
                               string06=string06)

    # webpage default settings
    use_optType = "Strong"
    description = SearchDataBase("Options", "Desc", "Name", use_optType)
    _length = SearchDataBase("Options", "NumbOfChars", "Name", use_optType)
    _useUpper = SearchDataBase("Options", "UCase", "Name", use_optType)
    _useLower = SearchDataBase("Options", "LCase", "Name", use_optType)
    _useNumber = SearchDataBase("Options", "Numb", "Name", use_optType)
    _useSpecial = SearchDataBase("Options", "Special", "Name", use_optType)
    _excludeAmbiguous = SearchDataBase("Options", "ExcludeAmbiguous", "Name", use_optType)
    
    
    string01 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
    string02 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
    string03 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
    string04 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
    string05 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
    string06 = gen_custom_pass(_length, _useUpper, _useLower, _useNumber, _useSpecial, _excludeAmbiguous)
        
    return render_template('index.html',
                           _dropdown1List=_dropdown1List,
                           whatToGen=use_optType,
                           _description=description,
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

