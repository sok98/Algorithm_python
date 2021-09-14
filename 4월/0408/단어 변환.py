def solution(begin, target, words):
    answer = 0
    queue = [begin]

    while True:
        temp_queue = []
        for word_1 in queue:

            if word_1 == target:
                return answer

            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                # word_1과 word_2의 철자 중 한글자만 같지 않다면
                if sum([x != y for x, y in zip(word_1, word_2)]) == 1:
                    temp_queue.append(words.pop(i))

        if not temp_queue:
            return 0
        queue = temp_queue
        answer += 1


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
