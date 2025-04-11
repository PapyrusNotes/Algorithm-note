from django.db import models
from django.db.models import F

class Counter(models.Model):
    id=models.IntegerField(unique=True, primary_key=True)
    count = models.IntegerField(default=0)

def increment(id):
    counter = Counter.object.get(id=id)
    counter.count = counter.count + 1
    counter.save()

# race condition
# 다른 트랜잭션이 +1을 했을 때 consistency가 훼손됨.
# lock 걸기
# application server로 가지고 오지 말고 db에서 직접 카운트 + 1
