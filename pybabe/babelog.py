
from base import StreamHeader, BabeBase, StreamMeta
import csv


class log_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ','
    doublequote = False
    escapechar = '\\'
    quoting = csv.QUOTE_MINIMAL
    quotechar = '"'

def log(stream, logfile):
    if isinstance(logfile, basestring):
        logstream = open(logfile, 'wb')
        do_close = True
    else:
        logstream = logfile
        do_close = False
    for row in stream:
        if isinstance(row, StreamHeader):
            writer = csv.writer(logstream, log_dialect)
            writer.writerow(row.fields)
        elif isinstance(row, StreamMeta):
            pass
        else:
            writer.writerow(list(row))
        yield row
    if do_close:
       logstream.close()
       
BabeBase.register("log", log)