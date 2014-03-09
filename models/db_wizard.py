### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_knowdb',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_preknow', type='string',
          label=T('Preknow')),
    Field('f_canknow', type='string',
          label=T('Canknow')),
    Field('f_simknow', type='string',
          label=T('Simknow')),
    Field('f_detail', type='string',
          label=T('Detail')),
    Field('f_contributor', type='string',
          label=T('Contributor')),
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_knowdb_archive',db.t_knowdb,Field('current_record','reference t_knowdb',readable=False,writable=False))

########################################
db.define_table('t_userdb',
    Field('f_username', type='string',
          label=T('Username')),
    Field('f_know', type='string',
          label=T('Know')),
    Field('f_project', type='string',
          label=T('Project')),
    Field('f_subscribe', type='string',
          label=T('Subscribe')),
    Field('f_follow', type='string',
          label=T('Follow')),
    format='%(f_username)s',
    migrate=settings.migrate)

db.define_table('t_userdb_archive',db.t_userdb,Field('current_record','reference t_userdb',readable=False,writable=False))
