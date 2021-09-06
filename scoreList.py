# Assessment Task

def assessScores (scoreList):
  for i in range (0, len(scoreList)):
    if (scoreList[i] >= 60):
      print ("Computer", i+1, "has *moderate* seccurity issues.")
    elif (scoreList[i] >= 80):
     print ("Computer", i+1, "has minor seccurity issues.")

    elif (scoreList[i] >= 100):
     print ("Computer", i+1, "has no known security issues.")
    else:
     print ("Computer", i+1, "has ***severe*** seccurity issues.")

  print ("Process complete: ", len(scoreList), "computers scanned")
  return

scores = [1,60,70,80,90]
assessScores (scores)
