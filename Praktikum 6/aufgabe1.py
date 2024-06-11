import time
import psutil
import multiprocessing
import testprogram_a1
import matplotlib.pyplot as plt


def get_memory_info(pid):
    process = psutil.Process(pid)
    mem_info = process.memory_full_info()
    return mem_info.rss, mem_info.vms, mem_info.uss  # RSS, VMS und Unique Set Size


def monitor_memory(pid):
    memory_values = []
    virtual_memory_values = []
    unique_memory_values = []
    while True:
        mem_usage, virtual_mem_usage, unique_mem_usage = get_memory_info(pid)
        print(f"Memory Usage (RSS): {mem_usage / (1024 ** 2)} MB")
        print(f"Virtual Memory Usage (VMS): {virtual_mem_usage / (1024 ** 2)} MB")
        print(f"Unique Memory Usage (USS): {unique_mem_usage / (1024 ** 2)} MB")
        memory_values.append(mem_usage)
        virtual_memory_values.append(virtual_mem_usage)
        unique_memory_values.append(unique_mem_usage)
        time.sleep(0.2)

        try:
            if not psutil.Process(pid).is_running():
                break
        except psutil.NoSuchProcess:
            break

    return memory_values, virtual_memory_values, unique_memory_values


def run_aufgabe1():
    # Start the testprogram_a1.start_aufgabe1() in a separate process
    process = multiprocessing.Process(target=testprogram_a1.start_aufgabe1)
    process.start()

    # Monitor memory usage of the new process
    memory_values, virtual_memory_values, unique_memory_values = monitor_memory(process.pid)

    process.join()
    return memory_values, virtual_memory_values, unique_memory_values

def run_aufgabe1_konventionell():
    # Start the testprogram_a1.start_aufgabe1_konventionell() in a separate process
    process = multiprocessing.Process(target=testprogram_a1.start_aufgabe1_konventionell)
    process.start()

    # Monitor memory usage of the new process
    memory_values, virtual_memory_values, unique_memory_values = monitor_memory(process.pid)

    process.join()
    return memory_values, virtual_memory_values, unique_memory_values

def plot_memory_usage(memory_values, virtual_memory_values, unique_memory_values):
    time_stamps = [i * 0.2 for i in range(len(memory_values))]  # Assuming data is collected every 0.5 seconds
    plt.figure(figsize=(10, 5))
    plt.plot(time_stamps, [mem / (1024 ** 2) for mem in memory_values], label='Memory Usage (RSS) (MB)')
    plt.plot(time_stamps, [v_mem / (1024 ** 2) for v_mem in virtual_memory_values], label='Virtual Memory Usage (VMS) (MB)')
    plt.plot(time_stamps, [u_mem / (1024 ** 2) for u_mem in unique_memory_values], label='Unique Memory Usage (USS) (MB)')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Usage (MB)')
    plt.title('Memory Usage Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    memory_values, virtual_memory_values, unique_memory_values = run_aufgabe1()
    plot_memory_usage(memory_values, virtual_memory_values, unique_memory_values)

    memory_values, virtual_memory_values, unique_memory_values = run_aufgabe1_konventionell()
    plot_memory_usage(memory_values, virtual_memory_values, unique_memory_values)