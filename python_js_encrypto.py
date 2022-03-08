import execjs # require('jsdom')

# pip install pyexecjs   npm install -g jsdom
def js_encrypto(public_key, password):
    jsdom_code = '''
    var jsdom = require('jsdom');
    var { JSDOM } = jsdom;
    var { document } = (new JSDOM('<!doctype html><html><body></body></html>')).window;
    document = document;
    window = document.defaultView;
    var JSEncrypt = require('C://Project//PythonProject//python_extract//jsencrypt.min.js');
    '''
    # jsencrypt_code = open("jsencrypt.min.js",'r').read()

    dologin_js_func = '''
    function doLogin(public_key, password) {
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(public_key);
        var pass_new = encrypt.encrypt(password);
        return pass_new;
    }
    '''
    # public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDaP+rYm6rqTMP565UmMU6YXq46KtAN3zwDSO8LNa15p0lJfsaY8jXY7iLsZqQZrGYr2Aayp6hYZy+Q+AMB/VUiSpD9ojPyOQ7r9jsf9jZbTOL4kj6iLZn37fEhp4eLvRgy5EJCyQoFyLCsgLechBTlYl2eA95C3j4ZUFhiV6WFHQIDAQAB'
    # password = '1234566'
    jsenv = execjs.compile(jsdom_code+dologin_js_func,cwd="C://Users//dell//AppData//Roaming//npm//node_modules")
    miwen = jsenv.call("doLogin", public_key, password)
    print("密码: ", password,"\n加密后: ", miwen)
    return miwen
