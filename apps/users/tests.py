from django.test import TestCase

# Create your tests here.
class F():
    def __call__(self, num):
        a,b = 0,1
        l = []

        for idx in  range(num):
            l.append(a)
            a,b = b, a+b
        return l


if __name__ == '__main__':
    f = F()
    print(f(8))