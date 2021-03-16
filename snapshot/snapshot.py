
import psutil
import time
import json
import argparse


class Snapshot:
    score = 0

    def __init__(self):
        Snapshot.score += 1
        self.time = time.asctime()
        self.cpu_percents = psutil.cpu_percent(interval=1, percpu=True)
        self.disk_usage = psutil.disk_usage("/")
        self.virtual_memory = psutil.virtual_memory()
        self.io_counters = psutil.disk_io_counters()
        self.net_counters = psutil.net_io_counters()

    def __str__(self):
        return 'SNAPSHOT {}: {}: {}, {}, {}, {}, {}'.format(
            Snapshot.score, self.time, self.cpu_percents, self.disk_usage,
            self.virtual_memory, self.io_counters, self.net_counters)


def write_file(file_t, snap):
    with open('snapshot.txt', 'a') as f:
        if file_t == 'text':
            f.write(snap)
        if file_t == 'json':
            f.write(json.dumps(snap))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--time_step', '-t', type=int, default=5, help='period snapshot in minutes')
    parser.add_argument('--file_format', '-f', choices=['text', 'json'],
                        default='text', help='file format to output file')
    args = parser.parse_args()
    write_file(args.file_format, str(Snapshot()))
    time.sleep(args.time_step * 60)


if __name__ == '__main__':
    while True:
        main()
