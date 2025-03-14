def line_generator(input_list):
    for index, line in enumerate(input_list, start=1):
        stripped_line = line.strip()  
        if stripped_line: 
            yield index, stripped_line


a = [" nelson ", "diogo", "lucas", " "]

for line_number, content in line_generator(a):
    print(f"Line {line_number}: {content}")