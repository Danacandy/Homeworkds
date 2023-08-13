# 1
# def is_admin(func):
#     def wrapper(*args, **kwargs):
#         user_type = kwargs.get("user_type")
#         if user_type != "admin":
#             raise ValueError("Permission denied")
#         return func(*args, **kwargs)
#     return wrapper


# @is_admin
# def show_customer_receipt(user_type: str):
#     print("Function passed")


# try:
#     show_customer_receipt(user_type='user')
# except ValueError as e:
#     print(e)

# show_customer_receipt(user_type='admin')

# 2
# def catch_errors(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print(f"Found 1 error during execution of your function: {type(e).__name__} {e}")
#     return wrapper


# @catch_errors
# def some_function_with_risky_operation(data):
#     print(data['key'])

# some_function_with_risky_operation({'foo': 'bar'})
# some_function_with_risky_operation({'key': 'bar'})

