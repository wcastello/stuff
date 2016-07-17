from threading import Thread, Semaphore
from collections import Counter
from os import scandir
from sys import stdout

NUM_THREADS = 20
RESULTS_FILE = 'counter_results.txt'
KEYWORDS_FILE = 'counter_dict.txt'

def startAllThreads(threads):
    for thread in threads:
        thread.start()


def joinAllThreads(threads):
    for thread in threads:
        thread.join()


def process_file(filename, local_counter, counter, lock):
    try:
        with open(filename, 'r') as f:
            for line in f:
                for word in (w.strip().replace('.', '').lower() for w in line.split(' ')):
                    if word in local_counter:
                        local_counter[word] += 1
    except UnicodeDecodeError:
        print('\nError reading file {}. File wont be processed.'.format(filename))
    lock.acquire()
    counter.update(local_counter)
    lock.release()


def load_dict(filename):
    print('Loading dictionary...', end='')
    words = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in (w.strip().replace('.', '').lower() for w in line.split(' ')):
                if word:
                    words[word] = 0
    print('Done.')
    return words


def update_results_file(filename, counter):
    with open(filename, 'w') as f:
        f.write('Keyword: Count\n\n')
        for keyword, count in sorted(counter.items()):
            f.write('{}: {}\n'.format(keyword, count))


def print_results(counter):
    print('---')
    print('Keyword: Count\n')
    for keyword, count in sorted(counter.items()):
        print('{}: {}'.format(keyword, count))
    print('---')


def main():
    dictionary = load_dict(KEYWORDS_FILE)
    if not dictionary:
        print('Empty dictionary, exiting.')
        return

    counter = Counter(dictionary) # this is going to be used by all threads

    lock = Semaphore()
    threads = []

    print('Processing files...', end='')
    for i, entry in enumerate(scandir('.')):
        if entry.name.endswith('.c') or entry.name.endswith('.py') or entry.name.endswith('.txt') and entry.is_file():
            threads.append(Thread(target=process_file, name='Thread-file-{}'.format(entry.name),
                args=(entry.name, Counter(dictionary), counter, lock)))
        # process blocks of NUM_THREADS files
        if (i+1) % NUM_THREADS == 0:
            startAllThreads(threads)
            joinAllThreads(threads)
            print('.', end='')
            stdout.flush()
            update_results_file(RESULTS_FILE, counter)
            threads = []

    # process what is left
    if threads:
        startAllThreads(threads)
        joinAllThreads(threads)
        update_results_file(RESULTS_FILE, counter)
    print('Done.\nResults saved to {}.'.format(RESULTS_FILE))

    print_results(counter)

if __name__ == '__main__':
    main()