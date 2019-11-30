class job():
    hike = 1.05

    def __init__(self, first, last, digits, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@ucalgary.ca'
        self.digits = digits
        self.salary = salary

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def raiseSalary(self):
        # or any instance.hike ex: app1.hike or app2.hike
        self.salary = int(self.salary * job.hike)


app1 = job('Kanishqk', 'Singh', 987654321, 10000)
app2 = job('Test', 'Case', 1604213, 20000)

print(app2.__dict__)
job.raiseSalary(app2)
print(app2.salary)

# print(job.fullName(app2))

# print(app1)
# print(app2)

# print(app1.email)

# print('{} {}'.format(app1.first, app1.last))

# app1.first = 'Kanishqk'
# app1.last = 'Singh'
# app1.email = 'Kanishhqk.Singh@ucalgary.ca'
# app1.digits = 987654321
#
# app2.first = 'Test'
# app2.last = 'Case'
# app2.email = 'Test.Case@ucalgary.ca'
# app2.digits = 987654321
