

subject=["c","c++","java","java","python","os","android","toc"]

print(subject)
print(subject[1])# 1 index print korbe
print(subject[2:])# 2 index theke print korbe
print(subject[-1])# last index print korbe
print("python" in subject)
print("c sharp" in subject)
print("c sharp"not in subject)
print(subject+["code-block",27])#subject er sathe print korbe just
print(subject*2)#subject digun banai print korbe
subject.append("sublime-text")#subject er sesh a jog hobe
print(len(subject))#subject er lenth ber korbe
subject.insert(5,"oop")#5 index a oop insert
print(subject)
subject.remove("toc")
subject.sort()#shorting kore subject er value dekhabe
print(subject)
subject.reverse()#shorting reverse kore dekhabe
print(subject)
subject.pop()#last value vanish kore dibe
print(subject)
print(subject.pop())#last vanish value print korbe
#subject.clear()#list faka kore dibe
print(subject)
subject2=subject.copy()
print(subject2)
#pos=subject.index("java")#index dekhabe
print(subject.index("java"))#index dekhabe
pos=subject.count("java")#item ta koto bar ase ta dekhabe
print(pos)


#range function#
num =list(range(10))# 0 to 10 show korbe
print(num)

num =list(range(5,11))# 5 to 10 show korbe
print(num)

num =list(range(5,101,5))# 5 to 100 show korbe, 5 bebodhan a
print(num)