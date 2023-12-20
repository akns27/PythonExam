class lineQueue:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size # 입력받은 size만큼 배열 생성
        # front와 rear가 아무 데이터도 없는 -1 인덱스를 가리키도록 초기화
        self.front = -1
        self.rear = -1
    
    def isEmpty(self): # 큐가 텅 비었는가?
        return self.rear == self.front 
        # rear와 front가 같은 인덱스를 가리키므로 둘 사이에 존재하는 데이터가 없음! 
    
    def isFull(self): # 큐가 꽉 찼는가?
        return self.rear == self.size - 1
        # 데이터 입력 연산을 진행하는 rear가 더 이상 가리킬 새로운 인덱스가 없음!
    
    def enQueue(self, item): # 큐 삽입 연산
        if not self.isFull(): # 데이터를 삽입할 인덱스가 남아있다면
            self.rear += 1 # rear를 빈 인덱스로 이동 후 삽입
            self.list[self.rear] = item
        else:
            print("Queue is overflow!") # 데이터가 넘치므로 오버플로우

    def deQueue(self): # 큐 삭제 후 반환 연산
        if not self.isEmpty(): # 삭제할 데이터가 남아있다면
            self.front += 1 # front를 삭제할 데이터 인덱스로 이동 후
            temp = self.list[self.front] # 삭제할 데이터 저장
            self.list[self.front] = None # 삭제
            return temp # 저장해 뒀던 데이터 반환
        else:
            print("Queue is underflow!") # 데이터가 없으므로 언더플로우

    def peek(self): # 스택 반환 연산
        if not self.isEmpty(): # 반환할 데이터가 남아있다면
            return self.list[self.front + 1] # front + 1 인덱스의 데이터 반환
        else:
            print("Queue is underflow!") # 데이터가 없으므로 언더플로우