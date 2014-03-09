# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

def knowdb_manage():
    form = SQLFORM.smartgrid(db.t_knowdb,onupdate=auth.archive)
    return locals()

def userdb_manage():
    form = SQLFORM.smartgrid(db.t_userdb,onupdate=auth.archive)
    return locals()

def userpage():
    return dict()

