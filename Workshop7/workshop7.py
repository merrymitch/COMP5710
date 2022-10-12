from http import client
from itertools import count
from venv import create
import hvac 
import random 

def makeConn():
    hvc_client = client = hvac.Client(url='http://127.0.0.1:8200', token='hvs.pKUTSoJ7cT7YPQS9uqIbzLtP' ) 
    return hvc_client 

def storeSecret( client,  secr1 , cnt  ):
    secret_path     = 'SECRET_PATH_' + str( cnt  )
    create_response = client.secrets.kv.v2.create_or_update_secret(path=secret_path, secret=dict(password =  secr1 ) )
    # print( type( create_response ) )
    # print( dir( create_response)  )

def retrieveSecret(client_, cnt_): 
    secret_path        = 'SECRET_PATH_' + str( cnt_  )
    read_response      = client_.secrets.kv.read_secret_version(path=secret_path) 
    secret_from_vault  = read_response['data']['data']['password']
    print('The secret we have obtained:')
    print(secret_from_vault)

if __name__ == '__main__': 
    clientObj    =  makeConn() 

    # Store and retrieve root_user
    secret2store = 'root_user'
    counter      = 0
    print('The secret we want to store:', secret2store)
    print('='*50)
    storeSecret( clientObj,   secret2store, counter )
    print('='*50)
    retrieveSecret( clientObj,  counter )
    print('='*50)

    # Store and retrieve test_password
    secret2store = 'test_password'
    counter      = 1
    print('The secret we want to store:', secret2store)
    print('='*50)
    storeSecret( clientObj,   secret2store, counter )
    print('='*50)
    retrieveSecret( clientObj,  counter )
    print('='*50)

    # Store and retrieve ghp_ahAyHoRwoQ
    secret2store = 'ghp_ahAyHoRwoQ'
    counter      = 2
    print('The secret we want to store:', secret2store)
    print('='*50)
    storeSecret( clientObj,   secret2store, counter )
    print('='*50)
    retrieveSecret( clientObj,  counter )
    print('='*50)

    # Store and retrieve MTIzANO=
    secret2store = 'MTIzANO='
    counter      = 3
    print('The secret we want to store:', secret2store)
    print('='*50)
    storeSecret( clientObj,   secret2store, counter )
    print('='*50)
    retrieveSecret( clientObj,  counter )
    print('='*50)

     # Store and retrieve t5f28U
    secret2store = 't5f28U'
    counter      = 4
    print('The secret we want to store:', secret2store)
    print('='*50)
    storeSecret( clientObj,   secret2store, counter )
    print('='*50)
    retrieveSecret( clientObj,  counter )
    print('='*50)