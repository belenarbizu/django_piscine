import sys


def create_list(content: list) -> list:
    final_list = []
    for line in content:
        parts = line.split(' = ')
        name = parts[0]
        attributes = parts[1].split(', ')
        element_data = [name]
        for attr in attributes:
            element_data.append(attr.split(':')[1])
        final_list.append(element_data)
    return final_list


def create_html(elements_list: list):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Periodic Table</title>
</head>
<body>
    <table>
        <tr>"""

    current_pos = 0
    for element in elements_list:
        pos = element[1]
    
        if pos < current_pos:
            html += "        </tr>\n        <tr>"
            current_pos = 0

        while current_pos < pos:
            html += '<td style="border: 1px solid white; padding:10px"></td>'
            current_pos += 1

        html += f"""<td style="border: 1px solid black; padding:10px">
                <h4>{element[0]}</h4>
                <ul>
                    <li>No {element[2]}</li>
                    <li>{element[3]}</li>
                    <li>{element[4]}</li>
                    <li>{element[5]} electron</li>
                </ul>
            </td>"""
        current_pos += 1

    html += """
        </tr>
    </table>
</body>
</html>"""

    with open('periodic_table.html', 'w') as f:
        f.write(html)


def change_pos_int(elements_list: list) -> list:
    for element in elements_list:
        element[1] = int(element[1])
        element[2] = int(element[2])
    return elements_list


def main():
    try:
        with open('periodic_table.txt') as f:
            content = f.read().strip().split('\n')
        elements_list = create_list(content)
        elements_list = sorted(elements_list, key=lambda x: (int(x[2]), int(x[1])))
        elements_list = change_pos_int(elements_list)
        create_html(elements_list)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()