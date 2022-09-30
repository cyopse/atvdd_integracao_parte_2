from emulated_database import user_Register
#from unittest.mock import patch


#Unitarios

#def register_Test_Without_Double():
#    assert not user_Register(
#        {'lucas': 'teixeira'}
#    )

#def register_Test_With_Double():
#    with patch('emulated_database.validate') as validator:
#        validator.return_value = False
#        
#        assert not user_Register(
#            {'lucas': 'teixeira'}
#        )

#Integração

def register_no_success(db):
    assert not user_Register(
        {'lucas': 'teixeira'}
    )
    assert db.db == []

def check_db_for_user(db):
    user = {'lucas': 'teixeira'}
    user_Register(user)
    assert db.user.query(user['lucas'])
    
