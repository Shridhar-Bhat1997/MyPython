# zip()--> aggregates elements from two or more iterables(list,tuples,sets etc)
# creates a zip object with paired elements stored in tuples for each element...

usernames=["Dude","Milan","Joel"]
passwords=("abx@pass","abc24","hrd90")
login_date=["1/1/2021","2/4/2020","2/5/2022"]

users=zip(usernames,passwords,login_date)

print(type(users))

for i in users:
    print(i)