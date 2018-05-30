import re


class Table():
    def __init__(self):
        pass

    def table(self, name, header):
        head = ''
        lengths = []
        for elem in header:
            head += (f'| {elem} ')
            lengths.append(len(elem))

        lines = empty_line = '|'
        for i, elem in enumerate(lengths):
            empty_line += ' ' * elem + '  |'
            lines += '-' + '-' * elem
            if i != len(lengths) - 1:
                lines += '-+'
            else:
                lines += '-|'

        lines += '\n'
        user_table = f'\n{name}\n{lines}{head}|\n{lines}{empty_line}\n{lines}'
        return user_table

    def insert_raw(self, table, *args, autho_inc=False, border_line=False):
        raws = re.findall(r'[^\n]+', table)

        new_raw = raws[4]   # rows (|  |  |)
        line = raws[1]      # line (|--+--|)

        def get_header(raws):
            return raws[0] + '\n' + raws[1] + '\n' + raws[2] + '\n' + raws[3]

        user_table = get_header(raws)   # header table

        b_line = '\n' + line if (border_line == True) else ''
        if autho_inc:
            for i, elem in enumerate(args):
                user_table += '\n' + new_raw[:2] + str(i + 1) + new_raw[3:] + b_line

                
        return user_table

t = Table()
s = t.table(name='Table 1', header=['#', 'Yan Frolov', 'Alex Sokolov', 'Genadiydhdhshdhs'])
# print(s)
s = t.insert_raw(s, ['10', '17', 'how about no?'], ['a', 'hello', 'c'], ['1', 'raw', 's'], autho_inc=True)
print(s)
