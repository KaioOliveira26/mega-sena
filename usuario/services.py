import jwt
from django.contrib.auth.models import User

def validate_token_user(header):
    jwt_options = {
            'verify_signature': False,
            'verify_exp': True,
            'verify_nbf': False,
            'verify_iat': True,
            'verify_aud': False
        }

    try:
        decodedToken = jwt.decode(header['auth-token'],algorithms=["HS256"],options = jwt_options)
    except:
        return {'response':'token de autentificação invalido ou não foi fornecido','status':400}
    
    try:
        user_object = User.objects.get(id=decodedToken['user_id'])
    except:
        return {'response':'Usuário não encontrado','status':400}
    
    if user_object.is_active == False:
        return {'response':'Usuário foi excluido','status':203}
    
    return {'response':True,'user':user_object} 
