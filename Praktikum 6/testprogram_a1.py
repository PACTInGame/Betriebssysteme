import mmap
import time


def start_aufgabe1():
    # 1. Legen Sie eine große Datei von 1 GByte auf der Platte an.
    file_size = 1 * 1024 * 1024 * 1024  # 1 GB = 1.073.741.824 Bytes
    file_name = 'testfile.bin'
    time.sleep(1)
    # Erstellen einer Datei mit der Größe von 1 GB
    with open(file_name, 'wb') as f:
        f.write(b'\0' * file_size)
    time.sleep(1)
    # 2. Mappen Sie diese Datei in den Speicherbereich eines Testprogramms.
    with open(file_name, 'r+b') as f:
        mmapped_file = mmap.mmap(f.fileno(), 0)
        time.sleep(1)
        # 3. Schreiben Sie ins „mapped-Memory“ wie in ein lokales Array
        data_to_write = (
                    'A' * 100 + '\n').encode()  # Passt 10.631.107 mal in 1 GB, damit 1.073.741.807 Bytes: Es bleiben 17 Bytes übrig (\x00).
        length_of_data = len(data_to_write)
        time.sleep(1)
        for i in range(0, file_size - length_of_data + 1, length_of_data):
            mmapped_file[i:i + length_of_data] = data_to_write
        time.sleep(1)
        # 5. Heben Sie das Dateimapping wieder komplett auf.
        mmapped_file.close()
        time.sleep(1)

    # 6. Nach Ende des Testprogramms geben Sie Anfang und Ende Ihrer Datei aus
    def read_file_section(file_name, start, length):
        with open(file_name, 'rb') as f:
            f.seek(start)
            return f.read(length)

    print("Anfang der Datei:")
    print(read_file_section(file_name, 0, 1024))

    print("\nEnde der Datei:")
    print(read_file_section(file_name, file_size - 1024, 1024))
    time.sleep(1)


def start_aufgabe1_konventionell():
    # 1. Legen Sie eine große Datei von 1 GByte auf der Platte an.
    file_size = 1 * 1024 * 1024 * 1024  # 1 GB = 1.073.741.824 Bytes
    file_name = 'testfile.bin'
    time.sleep(1)
    # Erstellen einer Datei mit der Größe von 1 GB
    with open(file_name, 'wb') as f:
        f.write(b'\0' * file_size)
    time.sleep(1)

    # 2. Öffnen Sie die Datei für Lese- und Schreibzugriffe.
    with open(file_name, 'r+b') as f:
        time.sleep(1)
        # 3. Schreiben Sie in die Datei wie in ein lokales Array
        data_to_write = ('A' * 100 + '\n').encode()  # Passt 10.631.107 mal in 1 GB, damit 1.073.741.807 Bytes: Es bleiben 17 Bytes übrig (\x00).
        length_of_data = len(data_to_write)
        time.sleep(1)
        for i in range(0, file_size - length_of_data + 1, length_of_data):
            f.seek(i)
            f.write(data_to_write)
        time.sleep(1)

    # 6. Nach Ende des Testprogramms geben Sie Anfang und Ende Ihrer Datei aus
    def read_file_section(file_name, start, length):
        with open(file_name, 'rb') as f:
            f.seek(start)
            return f.read(length)

    print("Anfang der Datei:")
    print(read_file_section(file_name, 0, 1024))

    print("\nEnde der Datei:")
    print(read_file_section(file_name, file_size - 1024, 1024))
    time.sleep(1)