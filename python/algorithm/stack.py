class Stack(list):
    push = list.append    # Insert
                          # Delete - 내장 pop 메소드 활용
    def is_empty(self):   # 데이터가 없는지 확인
        if not self:
            return True
        else:
            return False

    def peek(self):        # 최상단 데이터 확인
        return self[-1]