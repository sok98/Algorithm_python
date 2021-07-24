def solution(citations):
    citations = sorted(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0