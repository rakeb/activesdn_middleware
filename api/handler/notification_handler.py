import queue
import time

from middleware.python import python_api_caller

rule = None
notificationQueue = queue.Queue()


def handle_notification():
    global rule
    while True:
        global notificationQueue
        if not notificationQueue.empty():
            response = notificationQueue.get()
            print("Inside Thread notification handler, printing SDN Response: ", response)
            print("Inside Thread notification handler, printing SDN Rule: ", type(rule))
            try:
                python_api_caller.coa_caller(rule, response)
            except Exception as e:
                print(e)

        time.sleep(5)


def setRule(p_rule):
    global rule
    rule = p_rule


def getNotificationQueue():
    global notificationQueue
    return notificationQueue
