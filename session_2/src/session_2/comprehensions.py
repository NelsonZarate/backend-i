#args
def main(*args):
    return sum(args)

print("the sum of the args is ", main(1,2,3))


#kwargs
def kwargs(threshold,**kwargs):
    for kwarg in kwargs.values():
        if kwarg >= threshold:
            print(kwarg)
    return

kwargs(2,a=1,b=2,c=3)

#challenge
def users(*args, **kwargs):
    for users in kwargs :
        if users == "name" :  user_name = kwargs[users]
        if users == "age" : user_age = kwargs[users]
        if users == "city" : user_city = kwargs[users]
    user = {"Name":user_name,"city:":user_city,"age:":user_age}
    return user,args
print(users(name="nelson",age=20,city="albufeira"))