import openstack

# Enable debug
openstack.enable_logging(debug=False)

conn = openstack.connect(cloud='blue')


# Get VMs per project
for project in conn.list_projects():
    print("\
        Project Name: {}\t \
        Class Name: {}\t \
        Student ID: {}\t".format(project.name, project.description.split(' ')[0], project.description.split(' ')[3]))
    for vms in conn.list_servers(all_projects=True, filters={'project_id': project.id}):
        print("\
            Virtual Machines: {}\n".format(vms.name))

