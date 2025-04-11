from django.db import transaction

def create():
    with transaction.atomic():
        user=User.object.create(name="jaewon", age=30)
        set_name(user.id)
        user.age=31
        user.save()

def set_name(id):
    user =User.object.get(id=id)
    user.name = "donghae"
    user.save()

# <잘못된 점>
# target user object가 존재하는데 또 읽으려고 하고 있음. 낭비
# create직후 데이터가 바뀌었을 때, inconsistency 발생 가능

# <개선점>
# user id말고 user obj를 직접 전달
#