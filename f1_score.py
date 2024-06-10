import math

def exercise1(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int.')
        return
        
    if not isinstance(fp, int):
        print('fp must be int.')
        return 
        
    if not isinstance(fn, int):
        print('fn must be int.')
        return
    if (fp <= 0) or (fn <= 0) or (tp <=0):
        print('tp and fn and fp must be greater than zero.')
        return

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision + recall)

    print (f'The value of precision is {precision}')
    print(f'The value of recall is {recall}')
    print(f'The value of f1_score is {f1_score}')

exercise1(2, 3, 4)
exercise1('a', 3, 4)
exercise1(2, 'a', 4)
exercise1(2, 3, 'a')
exercise1(2, 3, 0)
exercise1(-2.1, 3, 0)