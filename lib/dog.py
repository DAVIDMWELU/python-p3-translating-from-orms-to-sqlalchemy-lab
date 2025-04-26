# lib/dog.py

def create_table(Base, engine):
    Base.metadata.create_all(engine)
    engine.dispose() 

def save(session, dog):
    session.add(dog)
    session.commit()
    session.close()  # <-- Close here!

def get_all(session):
    dogs = session.query(Dog).all()
    session.close()  # <-- Close here!
    return dogs

def find_by_name(session, name):
    dog = session.query(Dog).filter_by(name=name).first()
    session.close()  # <-- Close here!
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).filter_by(id=id).first()
    session.close()  # <-- Close here!
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter_by(name=name, breed=breed).first()
    session.close()  # <-- Close here!
    return dog

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    session.close()  # <-- Close here!
