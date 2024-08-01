from diff import Diff

for i in range(1,21):

    changes = Diff(f'source/{i}.txt')
    changes.save_file(f'new_source/{i}.txt')