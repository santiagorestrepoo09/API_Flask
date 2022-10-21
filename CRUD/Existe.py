import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from CRUD import Registros

def UsuarioExiste(nombre):
  print("Llego el nombre : " ,nombre  )
  BanderaUsuario = False
  if not firebase_admin._apps:
      cred = credentials.Certificate('/home/santiago/Escritorio/DEVELOP/PYTHON/Soporte/Soporte_Bacnkend/basepython-96cab-firebase-adminsdk-md57n-f1a95fe34a.json')
      default_app = firebase_admin.initialize_app(cred ,{'databaseURL' : 'https://basepython-96cab-default-rtdb.firebaseio.com/'})
  ref = db.reference("/usuarios/users/")
  best_sellers = ref.get()
  for key, value in best_sellers.items():
    print(value["Nombre"])
    if(value["Nombre"] == nombre):
      print("encontre a : " , nombre)
      BanderaUsuario =  True
  return BanderaUsuario
