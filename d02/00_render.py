#!/Users/narajaon/.brew/bin/python3
import re, sys

def init_vars():
    try:
        from settings import name, age, profession, title
        return {
                'name': name,
                'age': age,
                'profession': profession,
                'title': title
                }
    except ImportError:
        print('Not enough variables set in settings.py')
        return None

def readfile(filename):
    file = open(filename, 'r')
    for line in file:
        print(line)

def get_var(line, regex):
    pattern = re.compile(regex, re.M)
    return pattern.match(line)

def render_cv(filename, var_names):
    try:
        template = open(filename, 'r')
        html = open('myCV.html', 'w+')

        for line in template:
            formated = line.format(name = var_names['name'],
                title = var_names['title'],
                age = var_names['age'],
                profession = var_names['profession'])
            html.write(formated)

        template.close()
        html.close()
    except IOError:
        print('File handling ERROR')
    except KeyError:
        print('Invalid template')

if __name__ == '__main__':
    if len(sys.argv) == 2 and get_var(sys.argv[1], '.+\.template$'):
        var_names = init_vars()
        if var_names:
            render_cv(sys.argv[1], var_names)
    else: print('bad argument')
