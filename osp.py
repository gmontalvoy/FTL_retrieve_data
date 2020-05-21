from openstack import connection

# Auth headers
conn = connection.Connection(auth_url='AUTH_URL_HERE!',
                   username='opentlc-mgr',
                   password='REDACTED',
                   user_domain_id='default',
                   project_domain_id='default')

# Iterate over project list to find relevant ones
for project in conn.list_projects():

    if "-project" in project.name:
        print(project.name + "\t" + project.description)
    