from django.db import transaction

class UserService:
    def transfer_money(self, from_user_id, to_user_id, amount):
        with transaction.atomic():
            from_user = User.objects.select_for_update().get(id=from_user_id)
            to_user = User.objects.select_for_update().get(id=to_user_id)

            if from_user.balance < amount:
                raise InsufficientFundsError()

            from_user.balance -= amount
            from_user.save()

            to_user.balance += amount
            to_user.save()

    def transfer_money_between_users(self, user1_id, user2_id, amount):
        with transaction.atomic():
            self.transfer_money(user1_id, user2_id, amount + 1000)
	        self.transfer_money(user2_id, user1_id, amount - 1000)

# 데드락은 무엇인가요? 해결하기 위해서는 어떻게 하면 되나요?
# 위의 코드에서 잘못된 점은 무엇인가요? 그리고 해결 방법은 무엇인가요?

# 데드락
# 락이 걸린 어떤 자원에 대해
# 모든 프로세스(Tx or session) 중에 락을 해제할 프로세스가 없는 상태


@transaction.atomic
def viewfnc(request):
    # this code executes inside a transaction.
    do_stuff()

def viewfunc(request):
    # this code executes in autocommit mode
    do_stuff()
    with transaction.atomic():
        # this code executes inside a transaction.
        do_more_stuff()

"""
<Avoid catching exceptions inside atomic>
atomic 블록이 종료될 때,
django app은 정상적으로 탈출했는지, exception과 함께 종료됐는지 보고
commit을 할 지, roll back을 할 지 결정한다.
atomic block안에서 handling한다는 것은 django로부터 문제가 발생했다는 것을 숨기는 것.
-> 문제를 야기할 수 있음.
문제가 발생하면 django는 atomic block 끝에서 rollback을 시도함.
rollback 이전에 db쿼리를 실행하려고 시도할 경우
django는 transaction management error을 raise.
올바르게 db error을 잡는 방법은, atomic block 주위에서잡 는것.
raw sql query를 날릴 경우
django 의 동작은 명세되지 않으며, database에 의존한다.
"""