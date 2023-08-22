Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text  = 'this is python script'
>>> words = text.split()
>>> list(zip(words, words[1:]))
[('this', 'is'), ('is', 'python'), ('python', 'script')]
>>> list(zip(*[text[i:] for i in range(3)]))
[('t', 'h', 'i'), ('h', 'i', 's'), ('i', 's', ' '), ('s', ' ', 'i'), (' ', 'i', 's'), ('i', 's', ' '), ('s', ' ', 'p'), (' ', 'p', 'y'), ('p', 'y', 't'), ('y', 't', 'h'), ('t', 'h', 'o'), ('h', 'o', 'n'), ('o', 'n', ' '), ('n', ' ', 's'), (' ', 's', 'c'), ('s', 'c', 'r'), ('c', 'r', 'i'), ('r', 'i', 'p'), ('i', 'p', 't')]
