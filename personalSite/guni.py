
import multiprocessing
bind = "localhost:8000"
workers = multiprocessing.cpu_count()*2 + 1
