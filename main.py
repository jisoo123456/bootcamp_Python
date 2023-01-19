def document_info(func):  # decorator
    def new_functions(*args, **kwargs):
        print('running function:', func.__name__)
        print('positional arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, *kwargs)
        print('실행결과:', result)
        return result  #만일 이 문장이 없는데 print(sub_int())를 해버리면 none이 뜨게 된다. 프린트 하라했는데 return할 게 없기 때문
                       #대신 그냥 sub_int()면 none값 안 뜨고 그냥 지금 함수 식에 있는 프린트들만 출력되고 none값 안 생김
    return new_functions

@document_info
def sub_int(x, y):
    return x - y


sub_int(7 ,3)
