class RunTimeTooLong(Exception):
    def __init__(self, case_name, run_time):
        self.name = case_name
        self.value = run_time

    def __str__(self):
        return "Run Time Too Long Error: %s run time - %s s" % (self.name, self.value)
