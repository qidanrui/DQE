# encoding=utf-8
from exp_classify import main, write_result

if __name__ == '__main__':
    filename = '../../dataset/classify/magic_origin'
    filenames = {
        'origin': filename,
        'error': filename,
        'test': '../../dataset/classify/data_test_magic',
        'train': '../../dataset/classify/data_train_magic',
    }
    origin_schema = ['attr%d' % i for i in xrange(1, 11)] + ['class']
    used_attrs = ['attr%d' % i for i in xrange(1, 11)]

    epsilon_list = [1,1.5,2,2.5,3]
    neighbor_k_list = [10]
    result = main(epsilon_list, neighbor_k_list, [21, 451, 46, 254, 36], filenames, origin_schema, used_attrs)
    print result
    write_result(result, epsilon_list, neighbor_k_list, 'result/classification_accuracy_epsilon_magic.dat')
