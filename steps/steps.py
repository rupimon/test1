from behave import given, when, then
import os

@given(u'I execute the python script "{pythonfile}" that creates a text file with three lines')
def step_impl(context,pythonfile):
    os.system("C:\\test1\\Scripts\\python " + pythonfile)


@then(u'the file "{file}" should have {count} lines of text')
def step_impl(context,file,count):
    line_count = 0
    with open(file, 'r') as f:
        for line in f:
            line_count += 1

    if(line_count == int(count)):
        print("File has three lines.")
    else:
        print("File doesn't have three lines.")