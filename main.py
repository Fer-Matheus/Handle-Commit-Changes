from diff import Diff

while True:
    op = input('Do you want to handle changes for all files or just for one file? (all/one/stop): ')

    if op == 'stop':
        break

    if op == 'one':
        file = input('Enter the file number: ')
        changes = Diff(f'source/{file}.txt')
        changes.show_together()
        changes.save_file(f'new_source/{file}.txt')
    else :
        for i in range(1,21):

            changes = Diff(f'source/{i}.txt')
            changes.save_file(f'new_source/{i}.txt')