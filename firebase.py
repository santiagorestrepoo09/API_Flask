import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

##Cargar el json de certificado del proyecto firebase
firebase_sdk = credentials.Certificate('basepython-96cab-firebase-adminsdk-md57n-f1a95fe34a.json')
##HAcemos referencia a la base de datos que vamos a guardar los datos 
firebase_admin.initialize_app(firebase_sdk,{'databaseURL' : 'https://basepython-96cab-default-rtdb.firebaseio.com/'})

ref = db.reference('/usuarios')
user_ref = ref.child('users')
##user_ref.push({ "Nombre" : "bbbbbb",  "password" : "222"})



##Actualizar datos 

##hopper_ref = user_ref.child()

handle = db.reference('usuarios/users')

##print(ref.get())

ref = db.reference("/usuarios/users/")
best_sellers = ref.get()
print(best_sellers)
for key, value in best_sellers.items():
	print(value["Nombre"])
	print(value["Nombre"])