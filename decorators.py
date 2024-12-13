def uppar_decore(fun):
    def wrapper(name):
        result=fun(name)
        return result.upper()
    return wrapper


def tripple_decore(fun):
    def wrapper(sent):
        result=fun(sent)
        length=len(result)
        result+=str(length)
        return result
    return wrapper

@tripple_decore
@uppar_decore
def hello_name(name):
    return "hai  "  + name

print(hello_name('javhara'))
