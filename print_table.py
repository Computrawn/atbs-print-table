# Push to hub, but bring up to new standards in future.


def printTable(data):
    colWidths = [0] * len(data)
    for mainVal in range(len(data)):
        lengths = []
        for subVal in range(len(data[mainVal])):
            lengths.append(len(data[mainVal][subVal]))
            colWidths[mainVal] = sorted(lengths)[-1]
    for i in range(len(data[mainVal])):
        print(
            f"{data[0][i].rjust(colWidths[0])} | {data[1][i].rjust(colWidths[1])} | {data[2][i].rjust(colWidths[2])}"
        )


tableData_1 = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

tableData_2 = [
    ["apples", "oranges", "cherries", "banana", "kiwi"],
    ["Alice", "Bob", "Carol", "David", "Barbara"],
    ["dogs", "cats", "moose", "goose", "giraffe"],
]

printTable(tableData_1)
print()
printTable(tableData_2)
