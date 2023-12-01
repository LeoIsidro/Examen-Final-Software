# API REST para consultas sobre cuentas de usuario

from flask import Flask, jsonify, request
import requests
from clases import Cuenta


app = Flask(__name__)

BD=[]
c1=Cuenta("21345", "Arnaldo", 200, ["123", "456"])
c2=Cuenta("123", "Luisa", 400, ["456"])
c3=Cuenta("456", "Andrea", 300, ["21345"])

BD.append(c1)
BD.append(c2)
BD.append(c3)

                                  


# Función para obtener el saldo de una cuenta

@app.route('/billetera/contactos', methods=['POST'])
def contactos():
    try:
        cuenta = request.args.get('minumero')

        # Se obtiene la cuenta correspondiente
        cuenta_obj = next((c for c in BD if c.getNumero() == cuenta), None)

        if cuenta_obj:
            # Buscar los contactos de la cuenta
            contactos = cuenta_obj.getContactos()
            contactos_obj = []
            print(contactos)
            for c in contactos:
                for i in BD:
                    if i.getNumero() == c:
                        contactos_obj.append((i.getNumero(), i.getNombre()))
            return jsonify(contactos_obj), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@app.route('/billetera/pagar', methods=['POST'])
def billetera():
    try:
        cuenta = request.args.get('minumero')
        numero = request.args.get('numerodestino')
        monto = request.args.get('valor')

        # Se realiza la transacción
        cuenta_obj = next((c for c in BD if c.getNumero() == cuenta), None)
        cuenta_destino = next((c for c in BD if c.getNumero() == numero), None)

        if cuenta_obj and cuenta_destino:

            # Se verifica que la cuenta tenga el saldo suficiente
            if cuenta_obj.getSaldo() >= int(monto):
                cuenta_obj.pagar(numero, int(monto))
                cuenta_destino.recibir(cuenta, int(monto))
                return jsonify({"mensaje": "Realizado de forma exitosa"}), 200
            else:
                return jsonify({"error": "Saldo insuficiente"}), 404
        else:
            return jsonify({"error": "No existe la cuenta"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@app.route('/billetera/historial', methods=['POST'])
def historial():
    try:
        cuenta = request.args.get('minumero')

        # Se obtiene la cuenta correspondiente
        cuenta_obj = next((c for c in BD if c.getNumero() == cuenta), None)
        print(cuenta_obj.getNumero())

        if cuenta_obj:
            # Buscar los contactos de la cuenta
            data={}
            historial = cuenta_obj.historial_transacciones()
            data["saldo"]=cuenta_obj.getSaldo()
            data["Operaciones"]= {"pagos": [], "recibos": []}
            for h in historial:
                if h.tipo=="pago":
                    data["Operaciones"]["pagos"].append({"numero":h.NumeroDestino,"monto":h.Valor})
                else:
                    data["Operaciones"]["recibos"].append({"numero":h.NumeroDestino,"monto":h.Valor})
            return jsonify(data), 200
        else:
            return jsonify({"error": "No existe la cuenta"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 404


# correr la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)



