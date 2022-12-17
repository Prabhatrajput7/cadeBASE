def newly(fx):
    def wrapper():
        return fx()
    print('newly')
    return wrapper


@newly
def new():
    print('new')

# new()