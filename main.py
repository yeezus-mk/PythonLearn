from PythonLearn.Equations import Equations
from PythonLearn.people.Human import Human
from PythonLearn.people.Woman import Woman

print(Equations.linear(4, 5), Equations.square(1, -4, 4), Equations.cube(1, -4, 4, 0))

man = Human('Паша')
woman = Woman('Александра')
woman2 = Woman('София')
man2 = Human('Гена')
man.work()
children = Woman.sex(woman, woman2)