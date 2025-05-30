import json
import os



#ejoi-2024-1-ua.pdf -> ejoi-2024-1-UKR.pdf

def reformat():
    contest = 'ejoi'
    year = '2024'
    def make_error(text):
        print(text)
        assert False
    folder_dir = os.path.join(os.path.dirname(__file__), '../..')
    with open(os.path.join(folder_dir, '.github', 'scripts', '../data/al23.json'), 'r') as f:
        countries = json.load(f)
        al2to3 = {}
        for country in countries:
            al2to3[country['alpha2']] = country['alpha3']
        year_path = os.path.join(folder_dir, 'statements', contest, year)
        problems = 0
        max_problem = 0
        print(year_path)
        for problem in os.listdir(year_path):
            if problem == '.DS_Store':
                continue
            if not problem.isdigit():
                make_error('problem folder is not int ' + problem)
            if int(problem) <= 0 or int(problem) > 8:
                make_error('wrong problem ' + problem)
            problems += 1
            max_problem = max(max_problem, int(problem))
            problem_path = os.path.join(year_path, problem)
            for statement in os.listdir(problem_path):
                parts = statement.split('-')
                if len(parts) != 4:
                    make_error('wrong filename ' + statement)
                if parts[0] != contest:
                    make_error('wrong contest in filename ' + statement)
                if parts[1] != year:
                    make_error('wrong year in filename ' + statement)
                if parts[2] != problem:
                    make_error('wrong problem in filename ' + statement)
                name = parts[3]
                print(name)
                if name[-4:] != '.pdf':
                    make_error('wrong format of filename ' + statement)
                if len(name) != 6:
                    continue
                country = name[0:2].upper()
                print(country)
                print(al2to3[country])
                new_name = al2to3[country] + ".pdf"
                print(new_name)
                parts[3] = new_name
                new_file_name = "-".join(parts)
                print(new_file_name)
                print(problem_path)
                os.rename(os.path.join(problem_path, statement), os.path.join(problem_path, new_file_name))


reformat()
