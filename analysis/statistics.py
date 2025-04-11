import numpy as np

def compute_statistics(timestamps):
    interarrival_times = np.diff(timestamps)
    stats = {
        'Mean arrival time': np.mean(interarrival_times),
        'Median arrival time': np.median(interarrival_times),
        'Std arrival time': np.std(interarrival_times)
    }
    return stats
