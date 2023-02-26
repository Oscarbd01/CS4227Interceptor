import interceptor

def intercept(self, method):
    methodCalled = True
    print(f"Logging: {method} method called")

# def log_method_call(func):
#     def wrapper(*args, **kwargs):
#         logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper