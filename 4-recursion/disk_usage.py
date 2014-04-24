import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child = os.path.join(path, filename)
            total += disk_usage(child)
    print('{0:<7}'.format(total), path)
    return total

if __name__ == '__main__':
    print(disk_usage(os.getcwd()))
