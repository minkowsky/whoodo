from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.t_knowdb,10)
     populate(db.t_userdb,10)
