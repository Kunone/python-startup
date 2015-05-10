def announce_function_para(input_function):
    def new_function(*args, **kwargs):
        print 'Executing function: %s' %input_function.func_name
        input_function(*args, **kwargs)
    return new_function

@announce_function_para
def argument_show(*args, **kwargs):
    print 'Printing args: ', args
    print 'Printing kwargs: ', kwargs
argument_show(1,2,'cars', holiday='christmas')

@announce_function_para
def add_list(list_objects):
    print reduce(lambda x,y:x+y,list_objects)
add_list([1,2,3])
