# Add
>>> from yourapp import User
>>> me = User('admin', 'admin@example.com')
>>> db.session.add(me)
>>> db.session.commit()

# Delete
>>> me = User.query.get(1)
>>> db.session.delete(me)
>>> db.session.commit()

# Update
>>> me = User.query.get(1)
>>> me.email = 'edward@example.com'
>>> db.session.commit()
#------------------------------------------------------------------------------

# Retrieve a user by username:
>>> peter = User.query.filter_by(username='peter').first()
>>> peter.id
2
>>> peter.email
u'peter@example.org'

# Same as above but for a non existing username gives None:
>>> missing = User.query.filter_by(username='missing').first()
>>> missing is None
True

# Selecting a bunch of users by a more complex expression:
>>> User.query.filter(User.email.endswith('@example.com')).all()
[<User u'admin'>, <User u'guest'>]

# Ordering users by something:
>>> User.query.order_by(User.username).all()
[<User u'admin'>, <User u'guest'>, <User u'peter'>]

# Limiting users:
>>> User.query.limit(1).all()
[<User u'admin'>]

# Getting user by primary key:
>>> User.query.get(1)
<User u'admin'>

#------------------------------------------------------------------------------