def win_scores(a_scores, b_scores):
  a_total = sum(a_scores)
  b_total = sum(b_scores[:8])
  
  required = 0
  required =  a_total - b_total + 1
  return required
      
a_scores = list(map(int, input().split()))
b_scores = list(map(int, input().split()))
print(win_scores(a_scores, b_scores))