from datetime import datetime

def main():
    today = datetime.utcnow()

    hundred_days_of_code()


def hundred_days_of_code():
    """A function to make sure I code daily"""

    for day in range(100):
        wake_up()
        did_code = write_code(personal_project)

        if did_code:
            commit(did_code['changes'], 'git@github.com:bennett39')
            update_log(did_code['changes'], '100-days-of-code/log.md')
            day += 1

        other_work()
        goto_sleep()


if __name__ == '__main__':
    main()