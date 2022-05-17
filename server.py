from flask import Flask, request

app = Flask('__main__')


#Save a device
@app.route('/devices',methods=['POST'])
def save_device():
    device=request.json
    return device
    
@app.route('/devices',methods=['GET']) #SE EJECUTA METODO DESPUES DE LA RUTA DE /
def getdevice():
    return device

if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')