import pynamodb.constants
from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, NumberAttribute,
                                 UnicodeSetAttribute, UTCDateTimeAttribute)
from datetime import datetime


class TodoModel(Model):
    class Meta:
        billing_mode = pynamodb.constants.PAY_PER_REQUEST_BILLING_MODE
        table_name = 'yuri_todo_test'
        region = 'ap-northeast-2'

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(default='', null=False)
    last_modify_datetime = UTCDateTimeAttribute(default=datetime.utcnow())


'''
if not TodoModel.exists():
	TodoModel.create_table(wait=True,
                      billing_mode=pynamodb.constants.PAY_PER_REQUEST_BILLING_MODE)                   
'''
'''
def save():
    for i in range(5):
        thread_item = TodoModel('forum_name', 'forum_subject_1 '+str(i), last_post_datetime=datetime.utcnow())
        thread_item.save()

        thread_item = Thread('forum_name', 'forum_subject_2 ' + str(i), last_post_datetime=datetime.utcnow())
        thread_item.save()

    print('Save Done!')

def query():
    for item in Thread.query('forum_name', Thread.subject.startswith('forum_subject_2') ):
        print('Query returned item {0}'.format(item))


def update():
    thread_item = Thread.get('forum_name','forum_subject_1 1')
    thread_item.tags = ['52g studio']
    thread_item.save()
def delete_all():
    all_data = Thread.scan()
    print(list(all_data))
    all_data.delete()
    '''


if __name__ == '__main__':
    # save()
    # query()
    # update()
    # delete_all()
    print('Done!')
