# For loop with index, using enumerate()
first_names = [​'Bob'​, ​'Harry'​, ​'Marry'​]
for​ i, name ​in​ enumerate(first_names):
    print(​f'​{i}​. ​{name}​'​)
# >> ​0.​ Bob
# >> ​1.​ Harry
# >> ​2.​ Marry

# Class methods / types
- instance
- class
- static
- property

# String formatting
name = 'Edward'
print(​f'​{name}​ is eating.'​)
#--------------------------------------------------------------------------------------------

# * Format with comma and decimal point:
     '{0:,.2f}'.format(123.5)

# * Python Division to produce decimal values:
     from __future__ import division
     var = 5 / 7
     var = 0.7142857142857143

# * Python with MySQL
import MySQLdb
dbConn = MySQL.connect(host='xyz', user='xyz', passwd='xyz', db='xyz')
dictCursor = dbConn.cursor(MySQLdb.cursors.DictCursor)
dictCursor.execute("SELECT a,b,c FROM table_xyz")
resultSet = dictCursor.fetchall()
for row in resultSet:
    print row['a']
dictCursor.close
dbConn.close()

#-- datetime operation
import datetime
#- (A.) string to datetime object
    sched_start = '2015-02-26T15:00:00'  #- military time
    sched_start = datetime.datetime.strptime(sched_start, '%Y-%m-%dT%H:%M:%S')
#- (B.) datetime object to string
    sched_start = datetime.datetime.now()
    sched_start = sched_start.strftime('%Y-%m-%d')  #- will return in this format '2015-02-26'
#- (C.) add 'days' or 'hours' to a datetime value
    next_week = sched_start + datetime.timedelta(days=7)
##— Parse string datetime
from dateutil.parser import parse
datetime_temp = parse(src_timestamp)

#----------------------------------------------------------------------------------------------------------------
#-- export file
def beacons_export_to_csv(rec_search_val=None):
    app.logger.info('Beacons merchant export to csv')
    beacon_columns = [
        'beacon_id',
        'uuid',
        'major',
        'minor',
        'beacon_type_id',
        'latest_battery_level',
        'merchant_id',
        'beacon_id'
    ]
    search_filter = {}
    if rec_search_val != '':
        search_filter['$or'] = []
        search_filter['$or'].append({'tags': {'$regex': rec_search_val, '$options': '-i'}})  #-- tags
        for col in beacon_columns:
            if col in ['latest_battery_level', 'major', 'minor'] and rec_search_val.isdigit():
                search_filter['$or'].append({col: int(rec_search_val)})
            else:
                search_filter['$or'].append({col: {'$regex': rec_search_val, '$options': '-i'}})
    beacons = app.db.beacons.find(search_filter, {'beacon_id': True, 'uuid': True, 'major': True, 'minor': True})
    def generate():
        for beacon in beacons:
            yield beacon['beacon_id'] + ',' + beacon['uuid'] + ',' + str(beacon['major']) + ',' + str(beacon['minor']) + '\n'
    return Response(generate(), mimetype='text/csv', headers={'Content-Disposition': 'attachment; filename=beacons.csv'})
#----------------------------------------------------------------------------------------------------------------

#-- import CSV file
import csv
import sys
import codecs
def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]
def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')
with codecs.open('hz_zip.csv', encoding='utf-8') as csvfile:
    reader = unicode_csv_reader(csvfile, delimiter=',')
    for row in reader:
        print row
        # record = {
        #     'cc': row[0],
        #     'zc': row[1],
        #     'pn': row[2],
        #     'st': row[3],
        #     'pr': row[5]
        # }
#— Import Text File
    file = request.files['csv_file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        up_status = 'ok'
        print 'Upload ok', file.content_length, file.content_type, file.mimetype, file.headers
    elif file.filename != '':
        up_status = 'error'
        print 'File "%s" not allowed. CSV type only.' % (secure_filename(file.filename))
    if up_status == 'ok':
        virtual_numbers = []
        csv_duplicate_list = []
        line_no = process_cnt = 0
        try:
            for row in file:
                line = row.replace('\n', '').replace('"', '').replace("'", '').split(',')
                if line_no < 1:
                    line_no += 1
                    continue
                line_no += 1
                if len(line) < 3:
                    app.logger.warning('==> Invalid format in line #%s' % line_no)
                    up_status = 'error'
                    status_msgs.append('Invalid column format in file for line #%s' % line_no)
                    break
                homezone = line[0]
                vmsisdn = line[1]
                vnstatus = line[2]
          except Exception as e:
            print 'Exception error:', e
            return jsonify({'status': 'error', 'message': 'Processing Error. Please check the content of the file and try again.'})
          finally:
            file.close()

#-- Hash the list of dictionary
test = [{'id': 1, 'name': 'edward'}, {'id': 2, 'name': 'jose'}]
hashed = {d['id']:d for d in test}
## => output will be:
{
    1: {'id': 1, 'name': 'edward'},
    2: {'id': 2, 'name': 'jose'}
}
#----------------------------------------------------------------------------------------------------------------

# Random password generator for activation
import random
def generate_random_password():
     str = []
     chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
     for k in range(0, 8):
          str.append(random.choice(chars))
     return ''.join(str)
#— Parse Variable
source_val = 'Welcome {{name}}! Edward {{fullname}} jose!'
output = ''
splitted_val = source_val.split('{{')
output = '{}'.format(splitted_val[0])
ctr = 0
for item in splitted_val:
    ctr += 1
    if ctr > 1:
        keyword = item.split('}}')
        output = '{}{}{}'.format(output, keyword[0], keyword[1])
print output

#— Check variable type
if isinstance(var, int):
if not isinstance(filters, ObjectId):
    pass

#— Check variable type v2
>>> type(h)
<type 'str'>

#— ObjectId to datetime
row['_id'].generation_time

#— Get full stack trace of error
import traceback
try:
    raise ValueError
except:
    tb = traceback.format_exc()
else:
    tb = "No error"
finally:
    print tb

#— Python function with dynamic count of parameters
def SimpleMysql(**kwargs):
        conf = kwargs
        conf["keep_alive"] = kwargs.get("keep_alive", False)
        conf["host"] = kwargs.get("host", "localhost")
        conf["port"] = kwargs.get("port", 3306)
db = SimpleMysql(
    host="127.0.0.1",
    passwd="password",
    keep_alive=True
)

#— Get Age from birthdate
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#— Get request.form values
pprint(request.form)
print dict(request.form.iteritems())
iteritems(), iterkeys(), and itervalues()

#— Convert string item in list to ObjectID
location_ids = map(ObjectId, location_ids)

#— Date Format
"%d %b %Y %I:%M %p"  = "07 Aug 2016 @ 03:41 PM"

#— String Format
data = {'first': 'Hodor', 'last': 'Hodor!’}
'{first} {last}'.format(**data)
or
'{first} {last}'.format(first='Hodor', last='Hodor!')
-- or --
f'{self.id} ({self.book.title})'

#— http rest
import requests
…
try:
    result = requests.get('%s/api/cloud/health/nodes' % TEMP_CLOUD_URL, headers={'X-APIKey': TEMP_CLOUD_API})
    result = result.json()
    nodes = result['nodes']
except Exception as e:
    log.error(log_entry(session, 'Error! Cloud API "cluster_health()" error (%s)' % e))

#— Object Inspection
>>> foo = [1, 2, 3, 4]
>>> dir(foo)
['__add__', '__class__', '__contains__',
'__delattr__', '__delitem__', '__delslice__', ... ,
'extend', 'index', 'insert', 'pop', 'remove',
'reverse', 'sort']

#— Debugging scripts (and set a breakpoint)
import pdb
pdb.set_trace()
#— Jinja Templating
from jinja2 import Template
hotline_template = Template("""<include>
<extension name="emergency_protocol">
    <condition field="destination_number" expression="^{{ hotline['hotline_no'] }}$">
      {% for item in hotline['routes'] -%}
      <action application="log" data="${python(VBTS_Send_SMS_Direct {{ item }}|127.0.0.1|5062|1010|Return call to: +${effective_caller_id_number}")}/>
      {% endfor -%}
    </condition>
</extension>
""")
def update_hotline_xml(hotline):
  with open(HOTLINE_XML_FILE, 'w') as xml_file:
    xml_file.write(hotline_template.render(hotline=hotline))

#— Multiple if else
if 'div_cbx_hits_cnt' in widgets or 'div_cbx_logins_cnt' in widgets:
— into --
if any(key in widgets for key in (‘div_cbx_hits_cnt’, ‘div_cbx_logins_cnt’, .....)

#— Logging
import logging
log = logging.getLogger('logging-example')
#----
handler = logging.StreamHandler()
-- or --
handler = logging.FileHandler('/var/log/jasmin/some_file.log')
#----
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.INFO)
log.info('Got pdu: %s' % routable.pdu)

#— String Functions
'  hello  '.strip()  --> trim start/end whitespace

#-- Python Command line with arguments
#-- ex:   $ python test.py arg1 arg2 arg3
#!/usr/bin/python
import sys
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', sys.argv
Python Testing
https://laysrodriguesdev.wordpress.com/2017/06/28/how-to-play-around-with-python-and-mock/

# Script with input
user_input = input('Enter a hex number: ')
try:
    hexval = int(user_input, 12)
    print 'That is a valid hex value.'
except Exception as e:
    print e
    print 'That is an invalid hex value.'

# Root Path
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
-- or --
_basedir = os.path.abspath(os.path.dirname(__file__))

# Cleaner variable assignment to template
    vars = {
        'name': 'Ed',
        'address': 'Valenzuela'
    }
    return render_template('mikrotik_config/small.py', **vars)

# Human Friendly Values
>>> import humanfriendly
>>> user_input = raw_input("Enter a readable file size: ")
Enter a readable file size: 16G
>>> num_bytes = humanfriendly.parse_size(user_input)
>>> print num_bytes
16000000000
>>> print "You entered:", humanfriendly.format_size(num_bytes)
You entered: 16 GB
>>> print "You entered:", humanfriendly.format_size(num_bytes, binary=True)
You entered: 14.9 GiB

# Validator
>>> import validators
>>> validators.email('someone@example.com')
True
https://validators.readthedocs.io

# List Comprehension
http://book.pythontips.com/en/latest/index.html
squared = []
for x in range(10):
    squared.append(x**2)
# You can simplify it using list comprehensions. For example:
squared = [x**2 for x in range(10)]

# -- with if as filter --
for k, v in {k: v for k, v in query.items() if 'order[' in k and '][column]' in k}.items():

# Dict Comprehension
a = {v: k for k, v in some_dict.items()}
List to comma-delimited string
myList = ['a','b','c','d']
myString = ",".join(myList )

# Get client request vars
request.environ
example result:
{'wsgi.multiprocess': False, 'HTTP_COOKIE': 'reach.admin=eyJsb2dfZW1haWwiOnsiIGIiOiJZV0pqWkVCNVlXaHZieTVqYjIwPSJ9fQ.DKJSZQ.qoC2qExIn1IuvgMEEuvV3BbO7vs', 'SERVER_SOFTWARE': 'Werkzeug/0.12.2', 'SCRIPT_NAME': '', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/login/forgot-password', 'SERVER_PROTOCOL': 'HTTP/1.1', 'QUERY_STRING': '', 'werkzeug.server.shutdown': <function shutdown_server at 0x10c635050>, 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36', 'HTTP_CONNECTION': 'keep-alive', 'SERVER_NAME': '0.0.0.0', 'REMOTE_PORT': 59165, 'wsgi.url_scheme': 'http', 'SERVER_PORT': '8000', 'werkzeug.request': <Request '

# Client IP
request.remote_addr

# Client Browser
request.user_agent
# you may get like this:
# * user_agent.platform: windows
# * user_agent.browser: chrome
# * user_agent.version: 45.0.2454.101
# * user_agent.language: None
# * user_agent.string: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36

# Get/Remove first/last characters
>>> t = 'abcdefg'
* Get first '2 characters'
    >>> t[:2]
    'ab'
* Remove first '2 characters'
    >>> t[2:]
    'cdefg'
* Get last '2 characters'
    >>> t[-2:]
    'fg'
* Remove last '2 characters'
    >>> t[:-2]
    'abcde'

# Sort List of Dict by Key
from operator import itemgetter
newlist = sorted(list_to_be_sorted, key=itemgetter('name'))
# -- or --
newlist = sorted(list_to_be_sorted, key=itemgetter('name'), reverse=True)

# * Regular Expressions
ex: r'\d\d\d\d'
- To interpret this to python that its raw string
http://www.pythoncentral.io/introduction-to-python-regular-expressions/
* Python Classes
http://www.pythoncentral.io/introduction-to-python-classes/

# Merge 2 dict (python3)
>>> dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
>>> dict2 = {'bookC': 2, 'bookD': 4, 'bookE': 5}
>>> dict1.update(dict2)
>>> dict1
{'bookA': 1, 'bookB': 2, 'bookC': 2, 'bookD': 4, 'bookE': 5}

# Dict deepcopy (python3)
>>> import copy
>>> first = {'key': ['value']}
>>> second = copy.deepcopy(first)
>>> second['key'].append('second value')
>>> first
{'key': ['value']}
>>> second
{'key': ['value', 'second value']}
#--------------------------------------------------------------------------------------------

# Random Generator
>>> import random               # Python random module
>>> random.random()
0.5362880665009504
>>> random.randrange(12)
11
>>> random.randrange(12)
4
#--------------------------------------------------------------------------------------------

# Work with strings
>>> "hello".capitalize()        # Manipulate a string directly
                                # Capitalize string
'Hello'
>>> "hello".upper()             # Uppercase string
'HELLO'
>>> greet = "Hello There"       # Work with string variable
>>> greet[0]                    # String indexing
'H'                             # First character
>>> greet[6]
'T'                             # Seventh character
>>> greet[:4]                   # String slicing
'Hell'                          # First four characters
>>> greet[len(greet)-4:]
'here'                          # Last four characters
>>> greet[::-1]                 # Reverse a string
'erehT olleH'
>>> strPadded = "     My name is Nige   "
>>> strPadded.lstrip()
'My name is Nige   '            # Removing whitespace
>>> strPadded.rstrip()
'     My name is Nige'
>>> greet.replace("e","_")      # Replacing characters in a string
'H_llo Th_r_'
>>> greet.split()               # Splitting strings
['Hello', 'There']              # Default split is space
>>> greet.split("e")            # But can split on anything
['H', 'llo Th', 'r', '']
#--------------------------------------------------------------------------------------------

# Common Regex
# Symbol        Matches
. (dot)         Any single character
\d              Any single digit
[A-Z]           Any character between A and Z (uppercase)
[a-z]           Any character between a and z (lowercase)
[A-Za-z]        Any character between a and z (case-insensitive)
+               One or more of the previous expression (e.g., \d+ matches one or more digits)
[^/]+           One or more characters until (and not including) a forward slash
?               Zero or one of the previous expression (e.g., \d? matches zero or one digits)
*               Zero or more of the previous expression (e.g., \d* matches zero, one or more than one digit)
{1,3}           Between one and three (inclusive) of the previous expression (e.g., \d{1,3} matches one, two or three digits)
(...)           Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
#--------------------------------------------------------------------------------------------

# Run fake smtp server
$ python -m smtpd -n -c DebuggingServer localhost:8025

#-- Bultin HTTP server
$ python -m SimpleHTTPServer 8000
