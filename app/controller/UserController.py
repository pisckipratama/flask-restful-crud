from app.model.user import Users
from app import response, app

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "success retrieve data.")
    except Exception as e:
        print(e)

def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'data not found.')
        
        data = singleTransform(users)
        return response.ok(data, "success retrieve data.")

    except Exception as e:
        print(e)
    
def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }

    return data