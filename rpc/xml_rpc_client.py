import xmlrpc.client


def print_sessions(api, db, uid, password):
    sessions = api.execute_kw(db, uid, password, 'open_academy.session', 'search_read', [], {'fields': ['name', 'course_id', 'number_of_seats', ], })
    for record in sessions:
        course_id = record['course_id']
        print("Cours id: {0}; course name: {1}; session name: {2}; number of seats: {3}".format(course_id[0], course_id[1], record['name'], record['number_of_seats']))


host = input("Enter the hostname:")
port = input("Enter the port:")
db = input("Enter db name:")
user = input("Enter the user name:")
password = input("Enter your password:")

root = 'http://{0}:{1}/xmlrpc/'.format(host, port)

uid = xmlrpc.client.ServerProxy(root + 'common').login(db, user, password)
print("Logged in as %s (uid: %d)" % (user, uid))

api = xmlrpc.client.ServerProxy(root + 'object')

args = {
    "fields": ['name', 'number_of_seats']
}
print_sessions(api, db, uid, password)
# Create a new session
course_id = input("Specify the course ID from the list above:")
session_name = input("Enter a name of session:")
args = {
    'course_id' : course_id,
    'name' : session_name,
}
new_id = api.execute_kw(db, uid, password, 'open_academy.session', 'create', [args])
print_sessions(api, db, uid, password)
