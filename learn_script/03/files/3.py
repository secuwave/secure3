#!/usr/bin/python


def print_current_time():
    import datetime
    cur_time = datetime.datetime.now()
    print("current time: {}".format(cur_time))


print_current_time()


def print_yesterday():
    import datetime
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    print("yesterday: " + yesterday.strftime("%Y/%m/%d"))


print_yesterday()