def post_deploy(environment):
    """ This function is called by the main deploy in dye/tasklib after
    all the other tasks are done.  So this is the place where you can
    add any custom tasks that your project requires, such as creating
    directories, setting permissions etc."""
    dummy_task()


def dummy_task():
    """You can create many tasks callable individually, or just by
    post_deploy"""
    pass