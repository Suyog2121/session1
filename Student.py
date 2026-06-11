class student:
    fname = 'suyog'
    iname = 'girase'
    sub = 'computer'
    marks = 67.66

    def reading(self):
        print('student is reading the book')
    
    def playing(self):
        print('student is playing the cricket')

objstudent = student()
print(objstudent.fname)
print(objstudent.iname)
print(objstudent.sub)
print(objstudent.marks)
objstudent.reading()
objstudent.playing()
