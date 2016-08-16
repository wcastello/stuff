from threading import Thread, Semaphore
from collections import Counter
from os import scandir
from sys import stdout, argv
from copy import deepcopy

NUM_THREADS = 20
RESULTS_FILE_BASE = {'qa_corp': 'qacorp_res_',
                'qa_anal': 'qaanal_res_',
               'pres_corp': 'prescorp_res_',
               'pres_anal': 'presanal_res_'}

def startAllThreads(threads):
    for thread in threads:
        thread.start()


def joinAllThreads(threads):
    for thread in threads:
        thread.join()


specials = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
trans = str.maketrans(specials, ' '*len(specials))

def process_file(filename, local_counter, counter, lock):
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.translate(trans).upper()
                for sentence in local_counter['sentence_']:
                    local_counter['sentence_'][sentence] += line.count(sentence)
                for word in line.split(' '):
                    if word in local_counter['word_']:
                        local_counter['word_'][word] += 1
    except UnicodeDecodeError:
        print('\nError reading file {}. File wont be processed.'.format(filename))
    lock.acquire()
    counter['word_counter'].update(local_counter['word_'])
    counter['sentence_counter'].update(local_counter['sentence_'])
    lock.release()


def load_dict(filename):
    print('Loading dictionary...', end='')
    words = {'word_': {}, 'sentence_': {}}
    with open(filename, 'r') as f:
        for line in f:
            line = line.upper().strip()
            if line.find(' ') != -1:
                words['sentence_'][line] = 0
            else:
                words['word_'][line] = 0
    print('Done.')
    return words


def update_results_file(filename, counter):
    with open(filename, 'w') as f:
        f.write('Keyword/Sentence: Count\n\n')
        for keyword, count in sorted(counter['word_counter'].items()):
            f.write('{}: {}\n'.format(keyword, count))
        for sentence, count in sorted(counter['sentence_counter'].items()):
            f.write('{}: {}\n'.format(sentence, count))


def print_results(counter_pairs):
    for name, counter in counter_pairs.items():
        print('---{} counter ---'.format(name))
        print('Keyword/Sentence: Count\n')
        for keyword, count in sorted(counter['word_counter'].items()):
            print('{}: {}'.format(keyword, count))
        for sentence, count in sorted(counter['sentence_counter'].items()):
            print('{}: {}'.format(sentence, count))
        print('---')

def get_ftype(name):
    if name.find('qa_anal') != -1:
        return 'qa_anal'
    elif name.find('pres_corp') != -1:
        return 'pres_corp'
    elif name.find('qa_corp') != -1:
        return 'qa_corp'
    elif name.find('pres_anal') != -1:
        return 'pres_anal'

def get_results_fname(ftype, dict_name):
    return RESULTS_FILE_BASE[ftype] + dict_name.split('.')[0] + '.txt'

def main(argv):
    if len(argv) <= 1:
        print('Usage: {} <dict_file>'.format(argv[0]))
        return

    dict_file = argv[1]

    print('Would you like to load the dictionary {}? (y/n)'.format(dict_file))
    ans = input().lower()
    while ans not in {'y', 'n'}:
        print('Would you like to load the dictionary {}? (y/n)'.format(dict_file))

    if ans == 'n':
        print('Finished then!')
        return

    dictionary = load_dict(dict_file)
    if not dictionary:
        print('Empty dictionary, exiting.')
        return

    counter = {'sentence_counter': Counter(dictionary['sentence_']),
               'word_counter': Counter(dictionary['word_'])} # this is going to be used by all threads

    ftype_counters = {'qa_corp': counter,
                    'qa_anal': deepcopy(counter),
                      'pres_corp': deepcopy(counter),
                      'pres_anal': deepcopy(counter)}

    locks = {'qa_corp': Semaphore(),
            'qa_anal': Semaphore(),
             'pres_corp': Semaphore(),
             'pres_anal': Semaphore()}

    ftype_threads_d = {'qa_corp': [],
                'qa_anal': [],
               'pres_corp': [],
               'pres_anal': []}

    ftype_threads = deepcopy(ftype_threads_d)

    print('Processing files...', end='')
    for i, entry in enumerate(scandir('.')):
        if entry.name.endswith('.txt') and entry.is_file():
            ftype = get_ftype(entry.name)
            if not ftype:
                continue
            ftype_threads[ftype].append(Thread(target=process_file, name='Thread-file-{}'.format(entry.name),
                args=(entry.name, deepcopy(dictionary), ftype_counters[ftype], locks[ftype])))
        # process blocks of NUM_THREADS files
        if (i+1) % NUM_THREADS == 0:
            for ftype, threads in ftype_threads.items():
                startAllThreads(threads)
                joinAllThreads(threads)
                stdout.flush()
                results_file = get_results_fname(ftype, dict_file)
                update_results_file(results_file, ftype_counters[ftype])
            print('.', end='')
            ftype_threads = deepcopy(ftype_threads_d)

    # process what is left
    for ftype, threads in ftype_threads.items():
        if threads:
            startAllThreads(threads)
            joinAllThreads(threads)
            results_file = get_results_fname(ftype, dict_file)
            update_results_file(results_file, ftype_counters[ftype])

    print_results(ftype_counters)
    print('Results saved to (when available): ')
    for ftype in RESULTS_FILE_BASE:
        print('{}, '.format(get_results_fname(ftype, dict_file)), end='')
    print('Done.\n')

if __name__ == '__main__':
    main(argv)