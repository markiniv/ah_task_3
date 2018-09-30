def is_instance(some_list):
    for key, value in some_list.items():
        if isinstance(value, dict):
            answer_list.append(value)
            is_instance(value)
        else:
            answer_list.append(value)


def reverse_print(lst):
    is_instance(lst)
    print(answer_list[::-1])


answer_list = list()
some_list = {
  'value': 1,
  'next': {
    'value': 2,
    'next': {
      'value': 3,
      'next': {
        'value': 4,
        'next': None,
      },
    },
  },
}

reverse_print(some_list)
