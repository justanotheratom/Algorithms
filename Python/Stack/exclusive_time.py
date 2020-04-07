from typing import List
from Common.stack import Stack

def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    """
    Given a log file with start and end time log entries for various functions,
    return their exclusive execution times in a list, sorted by function id.
    >>> exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])
    [3, 4]
    >>> exclusiveTime(3, ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"])
    [1, 1, 2]
    """

    callstack = Stack()
    result = [0 for i in range(n)]
    currentTime = 0

    for i in range(len(logs)):
        le = parseLogEntry(logs[i])
        if le.operation == 'start':
            if not callstack.isempty():
                parentId = callstack.peek()
                result[parentId] += (le.timestamp - currentTime)
            callstack.push(le.id)
            currentTime = le.timestamp
        else:
            result[le.id] += (le.timestamp - currentTime + 1)
            currentTime = le.timestamp + 1
            callstack.pop()

    return result

def parseLogEntry(logLine):
    (id, operation, timestamp) = tuple(logLine.split(':'))
    return LogEntry(id, operation, timestamp)

class LogEntry(object):
    def __init__(self, id, operation, timestamp):
        self.id = int(id)
        self.operation = operation
        self.timestamp = int(timestamp)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
