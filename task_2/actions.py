import csv
from settings import csv_filename, csv_headers, input_colour, info_colour, confirm_response
import json
import tabulate
from misc import get_current_date


def add_record():
    record = dict()
    counter = 0
    for header in csv_headers:
        counter += 1
        # 5th column = date of completion, so its meaningless to type while its incompleted
        if counter == 6:
            if record[csv_headers[4]] in confirm_response:
                record[header] = input(input_colour + f"Please write record's {header} :")
            else:
                record[header] = ""
        else:
            record[header] = input(input_colour + f"Please write record's {header} :")

    print(info_colour + json.dumps(record, indent=2, default=str))
    response = input(input_colour + 'Its ok to proceed? ')
    if response in confirm_response:
        with open(csv_filename + ".csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if record['IS_DONE'] in confirm_response:
                record['IS_DONE'] = '1'
            else:
                record['IS_DONE'] = '0'
            writer.writerow(record.values())
            print(info_colour + 'Record successfully added.')
    else:
        print(info_colour + 'Canceled by user.')


def show_records(for_marking=False):
    data = list()
    with open(csv_filename + ".csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        if for_marking:
            for num, row in enumerate(reader, 0):
                if num:
                    data.append([num] + row)
        else:
            for row in reader:
                data.append(row)

        results = tabulate.tabulate(data)
    print(info_colour + results)


def show_help():
    print("".join(["1 = add an item,\n",
                   "2 = remove an item,\n",
                   "3 = mark an item as done,\n",
                   "4 = list item\n",
                   "5 = show simple statistic\n",
                   "0 = exit\n",
                   "h = show this message again"]))


def remove_item():
    show_records(True)
    print(info_colour + 'You can type several items using a coma (ex: 1,2,3)')
    response = input(input_colour + "Please type numbers of the items to delete: ")
    resp_list = response.split(',')
    if len(resp_list):
        curr_data = list()
        with open(csv_filename + '.csv', 'r') as inp:
            for num, row in enumerate(csv.reader(inp), 0):
                curr_data.append(row)

        resp_list.sort(reverse=True)

        for delete_index in resp_list:
            curr_data.pop(int(delete_index))

        with open(csv_filename + '.csv', 'w', newline='') as out:
            writer = csv.writer(out)
            for row in curr_data:
                writer.writerow(row)
        print(info_colour + 'Record(s) successfully deleted.')
    else:
        print(info_colour + "Got empty response, deletion canceled.")


def mark_items_as_done():
    show_records(True)
    print(info_colour + 'You can type several items using a coma (ex: 1,2,3)')
    response = input(input_colour + "Please type numbers of the items to mark as done: ")
    resp_list = response.split(',')
    if len(resp_list):
        curr_data = list()
        with open(csv_filename + '.csv', 'r') as inp:
            for num, row in enumerate(csv.reader(inp), 0):
                curr_data.append(row)

        for mark_as_done_index in resp_list:
            curr_data[int(mark_as_done_index)][4] = '1'
            curr_data[int(mark_as_done_index)][5] = get_current_date()

        with open(csv_filename + '.csv', 'w', newline='') as out:
            writer = csv.writer(out)
            for row in curr_data:
                writer.writerow(row)
        print(info_colour + 'Record(s) successfully marked as done.')
    else:
        print(info_colour + "Got empty response, marking items as done canceled.")


def show_simple_statistic():
    res = dict()
    with open(csv_filename + ".csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for num, row in enumerate(reader, 0):
            if num:
                if row[4] == '1':  # if is done
                    res[row[5]] = res.get(row[5], 0) + 1

    msg = ",\n".join([f"{val}: {key} task(s) done" for val, key in res.items()])
    print(info_colour + msg)


actions_dict = {
    "1": add_record,
    "add": add_record,
    "+": add_record,

    "2": remove_item,
    "r": remove_item,

    "3": mark_items_as_done,

    "4": show_records,
    "show": show_records,
    "list": show_records,
    "ls": show_records,

    "5": show_simple_statistic,

    "h": show_help,
    "help": show_help,
    "man": show_help,
}
