import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from CRUD import Existe

def GrabarJson(Nombre,password,Telefono,Ciudad):
    Respuesta = Existe.UsuarioExiste(Nombre)
    print("Respuesta : " , Respuesta)
    if Respuesta == False:
      print("usuario No existe ")
      entry = {"Nombre" :Nombre , "password" :password, "Telefono" :Telefono, "Ciudad" :Ciudad}
      if not firebase_admin._apps:
        cred = credentials.Certificate('basepython-96cab-firebase-adminsdk-md57n-f1a95fe34a.json') 
        default_app = firebase_admin.initialize_app(cred ,{'databaseURL' : 'https://basepython-96cab-default-rtdb.firebaseio.com/'})
      ref = db.reference('/usuarios')
      user_ref = ref.child('users')
      user_ref.push(entry)
    else:
      print("Usuario : " , Nombre ," YA existe ")
    return 